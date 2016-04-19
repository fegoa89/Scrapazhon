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

from scrapazhon.app_meta_data_scraper import AppMetaDataScraper

class AppMetaDataScraperTest(unittest.TestCase):

    def setUp(self):
        with open('scrapazhon/tests/integration/fixtures/app_page_html_response.json') as data_file:
            self.raw_html = json.load(data_file)

        self.response = AppMetaDataScraper(self.raw_html["response"]).collect_meta_data()

        return self.response

    def app_id_test(self):
        self.assertEqual(isinstance(self.response["app_id"], basestring), True)

    def app_name_test(self):
        self.assertEqual(isinstance(self.response["app_name"], basestring), True)

    def app_icon_test(self):
        self.assertEqual(url(self.response["app_icon"]), True)

    def screenshots_test(self):
        self.assertEqual(isinstance(self.response["screenshots"], list), True)

        for screenshot in self.response["screenshots"]:
            self.assertEqual(isinstance(screenshot, basestring), True)

    def categories_id_test(self):
        self.assertEqual(isinstance(self.response["categories_id"], list), True)

        for category in self.response["categories_id"]:
            self.assertEqual(isinstance(category, int), True)

    def keywords_test(self):
        self.assertEqual(isinstance(self.response["keywords"], list), True)

        for keyword in self.response["keywords"]:
            self.assertEqual(isinstance(keyword, basestring), True)        