import grabber
import common_funcs as cf
from bs4 import BeautifulSoup

class Processor:
    def __init__(self, url):
        self.url = url

    def grabcontent(self, **kwargs):
        """
        this function grabs the content of a webpage given by parameter url or default self.url
        """
        url = kwargs.get('url', self.url)

        branch = grabber.Branch(url)
        branch.pull()

        content = branch.contents

        #Saves all results in the variable soup in order to work with the data from content
        soup = BeautifulSoup(content, 'html.parser')

        #Below find all text associated with 'p' and from that it prints all text in a text version removing whitespaces with strip
        all_text = soup.find_all('p')

        for snippet in all_text:
            print (snippet.text.strip())

        #Below find the title
        #print(soup.title.prettify())


proc = Processor('https://ekstrabladet.dk/ferie/ikonisk-stenstatue-paa-paaskeoeen-er-oedelagt/8034294')
proc.grabcontent()
#proc.grabcontent(url = "https://ekstrabladet.dk/112/skud-i-boligkvarter-i-nat/8037296")
