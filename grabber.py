import requests
import re


class Spider:
    def __init__(self, url = "https://ekstrabladet.dk/"):
        self.url = url
        #self.pull()

    def pull(self):
        r = requests.get(self.url)
        self.contents = r.text

    def count(element):
        return self.contents.count(element)

    def getrawlinks(self, delim = "href"):
        indices = [c.start() for c in re.finditer(delim, self.contents)]
        #print(self.contents[indices[0]:])

        self.rawlinks = []
        for index in indices:
            first = self.contents[index:].index("\"") + index + 1
            second = self.contents[first:].index("\"") + first + 1
            #print(self.contents[first:second])
            self.rawlinks.append(self.contents[first:second])
