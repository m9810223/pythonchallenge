from collections import Counter
from pprint import pprint as pprint

from utils import get_comments
from utils import join_url


URL = 'http://www.pythonchallenge.com/pc/def/ocr.html'


if __name__ == '__main__':
    comments = get_comments(URL)
    comment, raw_data = comments
    print(comment)
    'find rare characters in the mess below:'

    counter = Counter(raw_data)
    # pprint(counter)

    result = ''.join(d for d in counter if counter[d] == 1)
    print(result)
    'equality'

    print(join_url(URL, f'{result}.html'))
    'http://www.pythonchallenge.com/pc/def/equality.html'
