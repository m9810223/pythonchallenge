import io
import struct
import zlib
from pprint import pprint as pprint

from utils import get_content
from utils import join_url
from utils import select_element


URL = 'http://www.pythonchallenge.com/pc/def/oxygen.html'


class Png:
    # https://www.w3.org/TR/png/#5Chunk-layout
    # https://www.w3.org/TR/PNG-Chunks.html
    # https://docs.python.org/3/library/struct.html#format-characters

    def __init__(self, buffer: io.BytesIO):
        self._buffer = buffer
        self.chunks: dict[str, list[bytes]] = {}
        self._check_signature()
        while self._read_chunk() != 'IEND':
            self._read_chunk()
        print(self.chunks.keys())
        # https://www.w3.org/TR/png/#11IHDR
        # TODO
        self.IHDR = self.chunks['IHDR'][0]
        self.width = int(struct.unpack('>I', self.IHDR[0:4])[0])
        self.height = int(struct.unpack('>I', self.IHDR[4:8])[0])
        self.bit_depth = int(struct.unpack('B', self.IHDR[8:9])[0])
        self.colour_type = int(struct.unpack('B', self.IHDR[9:10])[0])
        # https://www.w3.org/TR/png/#11pHYs
        # TODO
        self.pHYs = self.chunks['pHYs'][0]
        self.pixels_per_unit_x_axis = int(struct.unpack('>I', self.pHYs[0:4])[0])
        self.pixels_per_unit_y_axis = int(struct.unpack('>I', self.pHYs[4:8])[0])
        self.unit_specifier = self.pHYs[8:9]

    def _check_signature(self):
        # https://www.w3.org/TR/png/#3PNGsignature
        signature = self._buffer.read(8)
        assert b'\x89PNG\r\n\x1a\n' == signature

    def _read_chunk(self):
        (length,) = struct.unpack('>I', self._buffer.read(4))
        _chunk_type = self._buffer.read(4)
        chunk_type = _chunk_type.decode()
        chunk_data = self._buffer.read(length)
        (crc,) = struct.unpack('>I', self._buffer.read(4))
        # http://www.libpng.org/pub/png/spec/1.2/PNG-CRCAppendix.html
        assert crc == zlib.crc32(chunk_data, zlib.crc32(_chunk_type))
        self.chunks.setdefault(chunk_type, []).append(chunk_data)
        return chunk_type


if __name__ == '__main__':
    result = select_element(URL, 'img').attrs['src']
    print(result)
    'oxygen.png'

    url = join_url(URL, result)
    print(url)
    'http://www.pythonchallenge.com/pc/def/oxygen.png'

    content = get_content(url)
    png = Png(io.BytesIO(content))

    print(png.width)
    '629'

    print(png.height)
    '95'

    print(png.bit_depth, png.colour_type)
    '8 6'  # (red, green, blue, alpha)

    # https://www.w3.org/TR/png/#13Pixel-dimensions
    # TODO
    # d = zlib.decompress(b''.join(png.chunks['IDAT']))
    # print(d[0:1])
