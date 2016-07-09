# https://www.amazon.com/Best-Sellers-Appstore-Android/zgbs/mobile-apps/

import bs4

import scrapazhon

from bs4                              import BeautifulSoup
from scrapazhon.request               import Request
from scrapazhon.top_charts_scraper    import TopChartsScraper

import pprint
class TopChartsApps:

    def scrape(self):
        pprint.pprint(TopChartsScraper(self.top_paid_apps()).top_paid_apps())

    def top_paid_apps(self):
        return Request("https://www.amazon.com/Best-Sellers-Appstore-Android/zgbs/mobile-apps/").get_html_from_url()["response"]


TopChartsApps().scrape()