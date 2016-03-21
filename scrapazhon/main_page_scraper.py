from bs4 import BeautifulSoup
import time

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

        return listOfAppsInMainPage

    def appsInRow(self, row):
        rowHash             = {}
        appsArray           = []
        rowHash["apps"]     = []
        rowHash["rowLabel"] = row.find("h2", {"class": "s9Header"}).get_text()
        for app in row.select("a.title.ntTitle.noLinkDecoration"):
            appResult            = {}
            appResult["appName"] = app["title"]
            appResult["appId"]   = self.extractAppIDFromLink(app["href"])
            appResult["appIcon"] = self.appIconSelector(app.find("div", {"class": "imageContainer"}).find('img'))

            appsArray.append(appResult)

        rowHash["apps"] = appsArray

        return rowHash

    def extractAppIDFromLink(self, linkString):
        # HREF is built like /NBC-News-Digital-LLC-TODAY/dp/B00E5Q5GN6
        # where the last element is the id of the app.
        return linkString.split("/dp/")[1]

    def appIconSelector(self, imgElement):
        if imgElement.get("url") is None:
            return imgElement.get("src")
        else:
            return imgElement.get("url")