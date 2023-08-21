from utils import get_page
from utils import get_qs_dcit
from utils import join_url
from utils import replace_qs
from utils import select_element


URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'


if __name__ == '__main__':
    href = select_element(URL, 'center a').attrs['href']
    print(href)
    'linkedlist.php?nothing=12345'

    qs_dcit = get_qs_dcit(href)
    nothing = qs_dcit['nothing'][0]

    def find_next(current_nothing: str):
        nothing = current_nothing
        for i in range(1, 400):
            url = replace_qs(URL, dict(nothing=nothing))
            nothing = get_page(url).split()[-1]
            # print(i, nothing)
            if not nothing.isdigit():
                break
        return nothing

    result = find_next(nothing)
    print(result)
    'going.'

    result = find_next(result)
    print(result)
    'peak.html'

    print(join_url(URL, result))
    'http://www.pythonchallenge.com/pc/def/peak.html'
