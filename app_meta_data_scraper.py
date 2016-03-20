# Scraping metadata for a given app - "Peppa Pig: Holiday"
# page url link http://www.amazon.com/Entertainment-One-Ltd-Peppa-Pig/dp/B018IKM114/
# http://www.amazon.com/dp/B018IKM114

import bs4

import scrapazhon

from bs4                          	  import BeautifulSoup
from scrapazhon.request           	  import Request
from scrapazhon.app_meta_data_scraper import AppMetaDataScraper


class AppMetaData:
    def __init__(self, appId):
    	self.appId = appId
        self.url = self.buildAppPageUrl(self.appId)

    def scrape(self):
        AppMetaDataScraper(self.htmlResponse()).collectMetaData()

    def htmlResponse(self):
        return Request(self.url).getHtmlFromUrl()["response"]

    def buildAppPageUrl(self, appId):
    	return "http://www.amazon.com/dp/" + appId

AppMetaData("B018IKM114").scrape()