from bs4 import BeautifulSoup

class HtmlParser:
    def __init__(self, raw_html):
        ''' Constructor for this class. '''
        # Initializer
        self.raw_html = raw_html

    def mainPageApps(self):
        print("Parsing HTML")
        soup = BeautifulSoup(self.raw_html, "lxml")
        # Goes through all the rows (like "Games for You" or "Apps for you") on the main page
        for row in soup.select("div.a-section.unified_widget.rcm.widget.rcm.s9Widget"):
            print("*********************************************************************")
            # Within a row, each app is wrapped with a div that has a class
            # "fluid asin s9a0", where the last number represents the position of the app.
            # We'll gets apps until reach the limit for that row (normally the main page contains 7)
            count          = 0
            allAppsFounded = False
            # Row Label
            print("Row Label : " + row.find("h2", {"class": "s9Header"}).get_text())
            while (allAppsFounded == False):
                appContainer = "fluid asin s9a%s" % ( count )
                appInRow     = row.find("div", {"class": appContainer})
                if appInRow:
                    # App name
                    print("App Name : " + appInRow.find("span", {"class": "s9TitleText"}).get_text())
                    # App Icon
                    print("App Icon : " + appInRow.find("div", {"class": "imageContainer"}).find('img')["src"])
                    # imageContainer
                    count = count + 1
                else:
                    allAppsFounded = True