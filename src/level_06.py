import io
import zipfile
from pprint import pprint as pprint

from utils import get_comments
from utils import get_content
from utils import get_page
from utils import join_url


URL = 'http://www.pythonchallenge.com/pc/def/channel.html'


if __name__ == '__main__':
    comments = get_comments(URL)
    result, _ = comments
    print(result)
    ' <-- zip'

    url = URL.replace('.html', '.zip')
    content = get_content(url)
    # print(content)

    zip_file = zipfile.PyZipFile(io.BytesIO(content))
    # print(zip_file)

    # pprint(zip_file.namelist())
    '.....txt'
    'readme.txt'

    readme = zip_file.read('readme.txt').decode()
    print(readme)
    '''
    welcome to my zipped list.

    hint1: start from 90052
    hint2: answer is inside the zip
    '''

    nothing = '90052'
    nothings = [nothing]
    while True:
        content = zip_file.read(f'{nothing}.txt').decode()
        # print(content)
        nothing = content.split()[-1]
        if not nothing.isdigit():
            break
        nothings.append(nothing)
    print(content)
    'Collect the comments.'

    comments = ''.join(zip_file.getinfo(f'{x}.txt').comment.decode() for x in nothings)
    print(comments)
    result = 'HOCKEY'.lower()

    url = join_url(URL, f'{result}.html')
    result = get_page(url)
    print(result)
    '''it's in the air. look at the letters.'''

    result = 'OXYGEN'.lower()
    print(join_url(URL, f'{result}.html'))
    'http://www.pythonchallenge.com/pc/def/oxygen.html'
