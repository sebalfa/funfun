import grabber
import common_funcs as cf
from bs4 import BeautifulSoup

def my_function(x):
    branch = grabber.Branch(x)
    branch.pull()

    content = branch.contents

    """
    Saves all results in the variable soup in order to work with the data from content
    """
    soup = BeautifulSoup(content, 'html.parser')

    """
    Below find all text associated with 'p' and from that it prints all text in a text version removing whitespaces with strip
    """
    all_text = soup.find_all('p')

    for all_text in all_text:
        print (all_text.text.strip())

    """
    Below find the title
    print(soup.title.prettify())
    """

my_function('https://ekstrabladet.dk/ferie/ikonisk-stenstatue-paa-paaskeoeen-er-oedelagt/8034294')
