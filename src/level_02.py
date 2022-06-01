'http://www.pythonchallenge.com/pc/def/maketrans.html'


'''that's a handy little function. isn't it?'''


data = """map"""


a = ord('a')


for d in data:
    if 'a' <= d <= 'z':
        print(chr(a + (ord(d) + 2 - a) % 26), end="")
    else:
        print(d, end="")
print()

'ocr'


url = 'http://www.pythonchallenge.com/pc/def/ocr.html'


import requests


from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
file = BASE_DIR / f'{Path(__file__).name}.data'
if not file.is_file():
    response = requests.get(url)
    print(response.status_code)
    html = response.text
    file.write_text(html)
else:
    html = file.read_text()

from bs4 import BeautifulSoup
from bs4 import Comment

soup = BeautifulSoup(html, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
print(len(comments))
print(comments[0])
data = comments[1]


'''find rare characters in the mess below:'''


from collections import Counter


data = Counter(data)
from pprint import pprint

pprint(data)
data = ''.join(d for d in data)
print(data)


'equality'
