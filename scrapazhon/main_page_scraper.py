from bs4 import BeautifulSoup
import time

import pprint

class MainPageScraper:
    def __init__(self, raw_html):
        ''' Constructor for this class. '''
        # Initializer
        self.raw_html = raw_html

    def collectApps(self):
        print("Parsing HTML")
        soup = BeautifulSoup(self.raw_html, "lxml")
        listOfAppsInMainPage = []
        # Goes through all the rows (like "Games for You" or "Apps for you") on the main page
        for row in soup.select("div.a-section.unified_widget.rcm.widget.rcm.s9Widget"):
            listOfAppsInMainPage.append(self.appsInRow(row))

        pprint.pprint(listOfAppsInMainPage)

    def appsInRow(self, row):
        rowHash             = {}
        appsArray           = []
        rowHash["apps"]     = []
        rowHash["rowLabel"] = row.find("h2", {"class": "s9Header"}).get_text()
        for app in row.select("a.title.ntTitle.noLinkDecoration"):
            appResult = {}
            appResult["appId"]   = self.extractAppIDFromLink(app["href"])
            appResult["appName"] = app["title"]
            appResult["appIcon"] = app.find("div", {"class": "imageContainer"}).find('img').get("src")

            appsArray.append(appResult)

        rowHash["apps"] = appsArray

        return rowHash

    def extractAppIDFromLink(self, linkString):
        # HREF is built like /NBC-News-Digital-LLC-TODAY/dp/B00E5Q5GN6
        # where the last element is the id of the app.
        return linkString.split("/dp/")[1]