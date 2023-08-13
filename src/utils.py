from functools import partial
from urllib.parse import parse_qs
from urllib.parse import urlencode
from urllib.parse import urljoin as _urljoin
from urllib.parse import urlparse
from urllib.parse import urlunparse

import httpx_cache
from bs4 import BeautifulSoup as _BeautifulSoup
from bs4 import Comment
from bs4 import Tag


BeautifulSoup = partial(_BeautifulSoup, features='html.parser')


def get_page(url: str):
    return httpx_cache.Client(cache=httpx_cache.FileCache('.cache')).get(url).text


def get_redirect_url(url: str):
    content = select_element(url, 'META').attrs['content'].split(';')
    content = [x.strip() for x in content]
    prefix = 'URL='
    for c in content:
        if c.startswith(prefix):
            return join_url(url, c.removeprefix(prefix))
    return url


def get_comments(url: str):
    comments = tuple(
        map(
            str,
            BeautifulSoup(get_page(url)).find_all(
                string=lambda text: isinstance(text, Comment)
            ),
        )
    )
    print(f'{len(comments) = }')
    return comments


def select_element(url: str, selector: str):
    tag = BeautifulSoup(get_page(url)).select_one(selector) or Tag()
    return tag


def _get_qs(url: str):
    qs = urlparse(url).query
    return qs


def get_qs_dcit(url: str):
    qs_dcit = parse_qs(_get_qs(url))
    return qs_dcit


def replace_qs(url: str, qs_dict: dict[str, str]):
    new_url = urlunparse(urlparse(url)._replace(query=urlencode(qs_dict)))
    return new_url


def join_url(curr_url: str, target_url: str):
    new_url = _urljoin(curr_url, target_url)
    return new_url
