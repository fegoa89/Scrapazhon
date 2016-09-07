# Scraping metadata for a given app - "Peppa Pig: Holiday"
# page url link http://www.amazon.com/Entertainment-One-Ltd-Peppa-Pig/dp/B018IKM114/
# http://www.amazon.com/dp/B018IKM114

import bs4

import scrapazhon

from bs4                              import BeautifulSoup
from scrapazhon.request               import Request
from scrapazhon.app_meta_data_scraper import AppMetaDataScraper

import pprint

class AppMetaData:
    def __init__(self, app_id):
        self.app_id = app_id
        self.url = self.build_app_page_url(self.app_id)

    def scrape(self):
        pprint.pprint(AppMetaDataScraper(self.html_response()).collect_meta_data())

    def html_response(self):
        return Request(self.url).get_html_from_url()["response"]

    def build_app_page_url(self, app_id):
        return "https://www.amazon.com/gp/product/" + app_id

AppMetaData("B018IKM114").scrape()