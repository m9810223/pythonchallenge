from utils import join_url


URL = 'http://www.pythonchallenge.com/pc/def/0.html'


if __name__ == '__main__':
    result = 2**38
    url = join_url(URL, f'{result}.html')
    print(url)
    'http://www.pythonchallenge.com/pc/def/274877906944.html'
