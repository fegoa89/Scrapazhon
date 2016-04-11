import bs4

import scrapazhon

from bs4                          import BeautifulSoup

from scrapazhon.request           import Request

from scrapazhon.main_page_scraper import MainPageScraper

class MainPageApps:
    def __init__(self):
        self.url = "http://www.amazon.com/appstore"

    def scrape(self):
        MainPageScraper(self.html_response()).collect_apps()

    def html_response(self):
        return Request(self.url).get_html_from_url()["response"]

MainPageApps().scrape()