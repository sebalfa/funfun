import requests
import sys
import re


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    """
    since some of the articles pulled by grabber contains utf-8 characters,
    we print text using this function
    """
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

class Spider:
    def __init__(self, url = "https://ekstrabladet.dk/"):
        self.url = url
        #self.pull()

    def pull(self):
        r = requests.get(self.url)
        self.contents = r.text

    def count(element):
        return self.contents.count(element)

    def print(self):
        uprint(self.contents)

    def getrawlinks(self, delim = "href"):
        indices = [c.start() for c in re.finditer(delim, self.contents)]
        #print(self.contents[indices[0]:])

        self.rawlinks = []
        for index in indices:
            first = self.contents[index:].index("\"") + index + 1
            second = self.contents[first:].index("\"") + first + 1
            #print(self.contents[first:second])
            self.rawlinks.append(self.contents[first:second])


spider = Spider()
spider.pull()
spider.getlinks()
