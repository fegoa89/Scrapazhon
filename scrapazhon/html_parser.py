from bs4 import BeautifulSoup
import time
class HtmlParser:
    def __init__(self, raw_html):
        ''' Constructor for this class. '''
        # Initializer
        self.raw_html = raw_html

    def mainPageApps(self):
        print("Parsing HTML")
        soup = BeautifulSoup(self.raw_html, "lxml")
        listOfAppsInMainPage = []
        # Goes through all the rows (like "Games for You" or "Apps for you") on the main page
        for row in soup.select("div.a-section.unified_widget.rcm.widget.rcm.s9Widget"):
            listOfAppsInMainPage.append(self.appsInRow(row))

        return listOfAppsInMainPage

    def appsInRow(self, row):
        # Within a row, each app is wrapped with a div that has a class
        # "fluid asin s9a0", where the last number represents the position of the app.
        # We'll gets apps until reach the limit for that row (normally the main page contains 7)
        appCount          = 0
        stillAppsOnTheRow = True
        appsDictionary    = {}
        rowHash           = {}
        appsInRowList     = []
        while stillAppsOnTheRow:
            appContainer         = "fluid asin s9a%s" % ( appCount )
            appInRow             = row.find("div", {"class": appContainer})
            rowHash["row_label"] = row.find("h2", {"class": "s9Header"}).get_text()
            if appInRow:
                appsDictionary["app_name"] = appInRow.find("span", {"class": "s9TitleText"}).get_text()
                appsDictionary["app_icon"] = appInRow.find("div", {"class": "imageContainer"}).find('img')["src"]
                appsDictionary["app_id"]   = self.extractAppIDFromLink(appInRow.find("a", {"class": "title ntTitle noLinkDecoration"})["href"])
                appCount                   = appCount + 1
                appsInRowList.append(appsDictionary)
            else:
                rowHash["apps"]   = appsInRowList
                stillAppsOnTheRow = False

        return rowHash

    def extractAppIDFromLink(self, linkString):
        # HREF is built like /NBC-News-Digital-LLC-TODAY/dp/B00E5Q5GN6
        # where the last element is the id of the app.
        return linkString.split("/dp/")[1]