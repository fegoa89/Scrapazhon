from bs4 import BeautifulSoup
import time

class MainPageScraper:
    def __init__(self, raw_html):
        ''' Constructor for this class. '''
        # Initializer
        self.raw_html = raw_html

    def collect_apps(self):
        print("Parsing HTML")
        soup = BeautifulSoup(self.raw_html, "lxml")
        list_of_apps_in_main_page = []
        # Goes through all the rows (like "Games for You" or "Apps for you") on the main page
        for row in soup.select("div.a-section.unified_widget.rcm.widget.rcm.s9Widget"):
            list_of_apps_in_main_page.append(self.apps_in_row(row))

        return list_of_apps_in_main_page

    def apps_in_row(self, row):
        row_hash             = {}
        apps_array           = []
        row_hash["apps"]     = []
        row_hash["rowLabel"] = row.find("h2", {"class": "s9Header"}).get_text()
        for app in row.select("a.title.ntTitle.noLinkDecoration"):
            app_result            = {}
            app_result["appName"] = app["title"]
            app_result["appId"]   = self.extract_app_id_from_link(app["href"])
            app_result["appIcon"] = self.app_icon_selector(app.find("div", {"class": "imageContainer"}).find('img'))

            apps_array.append(app_result)

        row_hash["apps"] = apps_array

        return row_hash

    def extract_app_id_from_link(self, link_string):
        # HREF is built like /NBC-News-Digital-LLC-TODAY/dp/B00E5Q5GN6
        # where the last element is the id of the app.
        return link_string.split("/dp/")[1]

    def app_icon_selector(self, img_element):
        if img_element.get("url") is None:
            return img_element.get("src")
        else:
            return img_element.get("url")