import mock

import unittest

import scrapazhon

import bs4

from unittest           import TestCase

from scrapazhon.request import Request

from nose.tools         import *

from mock               import patch

from bs4 import BeautifulSoup

class RequestTest(unittest.TestCase):

    def valid_response_code_test(self):
        requestObject = Request("http://www.amazon.com/appstore")
        self.assertEqual(requestObject.getHtmlFromUrl()['code'], 200)
