import mock

import unittest

import scrapazhon

import bs4

import json

from unittest           import TestCase

from scrapazhon.request import Request

from nose.tools         import *

from mock               import patch

from bs4 import BeautifulSoup

class RequestTest(unittest.TestCase):

    def setUp(self):
        with open('scrapazhon/tests/integration/fixtures/main_page_html_response.json') as data_file:
            self.requestObject = json.load(data_file)

        return self.requestObject

    def valid_response_code_test(self):
        self.assertEqual(self.requestObject['code'], 200)

    # def valid_parsed_response_test(self):
        # Find amazon app store title on page
        # Commented for now - does not contain "Amazon Appstore" text anymore on page
        # soup = BeautifulSoup(self.requestObject['response'], "lxml")
        # self.assertEquals(soup.find("div", {"class": "acs-bgh1-header"}).text, '\nAmazon Appstore\n')