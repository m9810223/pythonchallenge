import io
import pickle
from pprint import pprint as pprint

from utils import get_page
from utils import join_url
from utils import select_element


URL = 'http://www.pythonchallenge.com/pc/def/peak.html'


def decode_line(line: list[tuple[str, int]]):
    return ''.join(char * amount for (char, amount) in line)


if __name__ == '__main__':
    result = select_element(URL, 'peakhell').attrs['src']
    print(result)
    'banner.p'

    url = join_url(URL, result)
    print(url)
    'http://www.pythonchallenge.com/pc/def/banner.p'

    result = pickle.load(io.BytesIO(get_page(url).encode()))
    # pprint(result)

    lines = '\n'.join(decode_line(line) for line in result)
    print(lines)
    result = 'channel'

    print(join_url(URL, f'{result}.html'))
    'http://www.pythonchallenge.com/pc/def/channel.html'
