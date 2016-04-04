import mock

import unittest

import scrapazhon

import bs4

import validators

import json

from validators import url

from unittest           import TestCase

from scrapazhon.request import Request

from nose.tools         import *

from mock               import patch

from bs4                import BeautifulSoup

from scrapazhon.main_page_scraper import MainPageScraper

class MainPageScraperTest(unittest.TestCase):

    def setUp(self):
        with open('scrapazhon/tests/integration/fixtures/main_page_html_response.json') as data_file:
            self.raw_html = json.load(data_file)

        return self.raw_html

    def collect_apps_main_response_test(self):
        # Tests that each hash within the response contains two keys:
        # rowLabel - key that represents the row title where this apps are displayed
        # apps - represents the apps listed within that label
        response = MainPageScraper(self.raw_html["response"]).collect_apps()

        for row_result in response:
            self.assertEqual(row_result.keys(), ['apps', 'rowLabel'])

    def app_dictionary_response_test(self):
        # Tests that each hash contains three keys with a valid format:
        # appIcon - app icon url            - url format
        # appId   - amazon app store app id - string
        # appName - Name of the app         - string
        response = MainPageScraper(self.raw_html["response"]).collect_apps()

        for row_result in response:
            for app_info in row_result['apps']:
                self.assertEqual(url(app_info["appIcon"]), True)
                self.assertEqual(isinstance(app_info["appName"], basestring), True)
                self.assertEqual(isinstance(app_info["appId"], basestring), True)
