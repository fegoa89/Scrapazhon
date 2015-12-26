from bs4 import BeautifulSoup

class HtmlParser:
    def __init__(self, raw_html):
        ''' Constructor for this class. '''
        # Initializer
        self.raw_html = raw_html

    def parse(self):
        print("Parsing HTML")
        soup = BeautifulSoup(self.raw_html, "lxml")
        # page title
        print(soup.title.string)
