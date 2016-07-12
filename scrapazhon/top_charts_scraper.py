from bs4 import BeautifulSoup

import time

import pprint

import parsedatetime

from datetime import datetime
from time     import mktime

class TopChartsScraper:
    def __init__(self, raw_html):
        self.raw_html = raw_html

    def top_paid_apps(self):
        top_paid_apps_array = []
        apps_in_page = self.soup_object().find("div", {"id":"zg_centerListWrapper"}).findAll("div", {"class":"zg_itemImmersion"})
        for app in apps_in_page:
            ranked_app = {}
            div_zg_title_dom_element     = app.find("div", {"class": "zg_title"}).find('a')
            ranked_app["rank_position"]  = self.sanitize_rank_position(app.find("span", {"class": "zg_rankNumber"}).get_text())
            ranked_app["app_title"]      = div_zg_title_dom_element.get_text()
            ranked_app["app_url"]        = div_zg_title_dom_element['href'].strip()
            ranked_app["app_id"]         = div_zg_title_dom_element['href'].strip().split("/dp/")[1].split("/")[0]
            ranked_app["app_icon_small"] = app.find("div", {"class": "zg_itemImageImmersion"}).find('a').find('img')['src'].strip()

            top_paid_apps_array.append(ranked_app)

        pprint.pprint(top_paid_apps_array)

    def sanitize_rank_position(self, ranked_position_string):
        return int(ranked_position_string.replace(".", ""))


    def soup_object(self):
        soup = BeautifulSoup(self.raw_html, "lxml")
        return soup