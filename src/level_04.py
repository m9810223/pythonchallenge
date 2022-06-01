URL = '''http://www.pythonchallenge.com/pc/def/linkedlist.php'''


from pathlib import Path

from utils import source_page

BASE_DIR = Path(__file__).parent.resolve()
file = BASE_DIR / f'{Path(__file__).name}.data'
page = source_page(URL, file)

from pyquery import PyQuery

html = PyQuery(page)

from urllib.parse import urlparse, urlunparse, urlencode, parse_qsl

href = html('center a').attr('href')
print(href)

qsl: list[tuple] = parse_qsl(urlparse(href).query)
print(qsl)
val = qsl[0][1]
print(val)


def get_val(start_val: str, index: int):
    val = start_val
    result = []
    for i in range(1, 400):
        qsl[0] = (qsl[0][0], val)
        url = urlunparse(urlparse(URL)._replace(query=urlencode(qsl)))
        val = PyQuery(url=url).text().split()[-1]
        result.append(val)
        print(i, val)
        if not val.isdigit():
            return


# get_val(val, 1)
get_val('going.', 86)
