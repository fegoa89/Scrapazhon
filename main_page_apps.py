import bs4

import scrapazhon

from bs4                          import BeautifulSoup

from scrapazhon.request           import Request

from scrapazhon.main_page_scraper import MainPageScraper

import pprint

class MainPageApps:
    def __init__(self):
        self.url = "https://www.amazon.com/appstore"

    def scrape(self):
        pprint.pprint(MainPageScraper(self.html_response()).collect_apps())

    def html_response(self):
        return Request(self.url).get_html_from_url()["response"]

MainPageApps().scrape()