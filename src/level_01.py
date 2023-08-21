from utils import get_redirect_url
from utils import join_url


URL = 'http://www.pythonchallenge.com/pc/def/274877906944.html'


DATA = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''


def _translate(char):
    if 'a' <= char <= 'z':
        return chr(ord('a') + (ord(char) + 2 - ord('a')) % 26)
    return char


def translate(string):
    return ''.join(_translate(x) for x in string)


if __name__ == '__main__':
    print(translate(DATA))
    '''i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.'''

    url = get_redirect_url(URL)
    'http://www.pythonchallenge.com/pc/def/map.html'

    result = translate('map')
    print(result)
    'ocr'

    print(join_url(URL, f'{result}.html'))
    'http://www.pythonchallenge.com/pc/def/ocr.html'
