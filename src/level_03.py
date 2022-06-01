URL = '''http://www.pythonchallenge.com/pc/def/equality.html'''


'''One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.'''


from pathlib import Path

from utils import source_page
from utils import get_comments

BASE_DIR = Path(__file__).parent.resolve()


if __name__ == '__main__':
    file = BASE_DIR / f'{Path(__file__).name}.data'
    page = source_page(URL, file)
    comments = get_comments(page)
    print(f'{len(comments) = }')
    data: str = comments[0].replace('\n', '')

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
            print(c, end='')

    'linkedlist'
