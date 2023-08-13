from utils import get_comments
from utils import get_page
from utils import join_url


URL = '''http://www.pythonchallenge.com/pc/def/equality.html'''


'''One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.'''


if __name__ == '__main__':
    comments = get_comments(URL)
    data: str = comments[0].replace('\n', '')

    result = ''
    for i, c in enumerate(data[4:-4], 4):
        if all(
            [
                c.islower(),
                data[i - 4].islower(),
                data[i - 3 : i].isupper(),
                data[i + 1 : i + 4].isupper(),
                data[i + 4].islower(),
            ]
        ):
            # print(data[i - 3 : i + 4])
            result += c
    print(result)
    'linkedlist'

    url = join_url(URL, f'{result}.html')
    print(url)
    'http://www.pythonchallenge.com/pc/def/linkedlist.html'

    result = get_page(url)
    print(result)
    'linkedlist.php'

    print(join_url(URL, result))
    'http://www.pythonchallenge.com/pc/def/linkedlist.php'
