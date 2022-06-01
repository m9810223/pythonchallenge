from functools import partial
from pathlib import Path

import requests
from bs4 import Comment
from bs4 import BeautifulSoup

BeautifulSoup = partial(BeautifulSoup, features='html.parser')


def source_page(url: str, file: Path):
    if not file.is_file():
        response = requests.get(url, verify=False)
        page = response.text
        file.write_text(page)
    else:
        page = file.read_text()
    return page


def get_comments(html):
    soup = BeautifulSoup(html)
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    return comments


def source_page_comments(*args, **kwargs):
    page = source_page(*args, **kwargs)
    comments = get_comments(page)
    return comments
