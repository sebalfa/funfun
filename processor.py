import grabber
import common_funcs as cf
from bs4 import BeautifulSoup

def my_function(x):
    branch = grabber.Branch(x)
    branch.pull()

    content = branch.contents

    #cf.uprint(content)
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.title.prettify())

my_function('https://ekstrabladet.dk/ferie/ikonisk-stenstatue-paa-paaskeoeen-er-oedelagt/8034294')
