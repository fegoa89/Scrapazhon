import bs4

import scrapazhon

from bs4                          import BeautifulSoup

from scrapazhon.request           import Request

from scrapazhon.main_page_scraper import MainPageScraper

class MainPageApps:
    def __init__(self):
        self.url = "http://www.amazon.com/appstore"

    def scrape(self):
        MainPageScraper(self.htmlResponse()).collectApps()

    def htmlResponse(self):
        return Request(self.url).getHtmlfromUrl()

MainPageApps().scrape()