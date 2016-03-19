import mock

import unittest

import scrapazhon

import bs4

from unittest           import TestCase

from scrapazhon.request import Request

from nose.tools         import *

from mock               import patch

from bs4                import BeautifulSoup

from scrapazhon.main_page_scraper import MainPageScraper

class MainPageScraperTest(unittest.TestCase):

    def setUp(self):
        self.rawHtml = Request("http://www.amazon.com/appstore").getHtmlFromUrl()["response"]
        return self.rawHtml

    def collect_apps_main_response_test(self):
        # Tests that each hash within the response contains two keys:
        # rowLabel - key that represents the row title where this apps are displayed
        # apps - represents the apps listed within that label
        response = MainPageScraper(self.rawHtml).collectApps()

        for rowResult in response:
            self.assertEqual(rowResult.keys(), ['apps', 'rowLabel'])

    def app_dictionary_response_test(self):
        # Tests that each hash within each app response contains three keys:
        # appIcon - app icon url
        # appId   - amazon app store app id
        # appName - Name of the app
        response = MainPageScraper(self.rawHtml).collectApps()

        for rowResult in response:
            for appInfo in rowResult['apps']:
                self.assertEqual(appInfo.keys(), ['appIcon', 'appId', 'appName'])
