import requests
import re


class Spider:
    """
    TODO: selectively grab urls for articles. Ignore meta-urls. Also, check if url already exists in branches.
    """
    def __init__(self, url = "https://ekstrabladet.dk/"):
        self.branches = []
        self.mainbranch = url
        self.info = []
        self.iter = 0

        self.crawl(url)
        print(self.info)


    def crawl(self, url):
        branch = Branch(url)
        branch.pull()

        self.info.append((url, branch.count("href")))

        self.iter +=1
        if self.iter > 5:
            return

        try:
            for subbranch in branch.getrawlinks():
                self.crawl(subbranch)
        except:
            pass


class Branch:
    def __init__(self, url):
        self.url = url
        #self.pull()

    def pull(self):
        r = requests.get(self.url)
        self.contents = r.text

    def count(self, element):
        return self.contents.count(element)

    def getrawlinks(self, delim = "href"):
        indices = [c.start() for c in re.finditer(delim, self.contents)]
        #print(self.contents[indices[0]:])

        self.rawlinks = []
        for index in indices:
            first = self.contents[index:].index("\"") + index + 1
            second = self.contents[first:].index("\"") + first + 1
            #print(self.contents[first:second])
            self.rawlinks.append(self.contents[first:second - 1])

        return self.rawlinks
