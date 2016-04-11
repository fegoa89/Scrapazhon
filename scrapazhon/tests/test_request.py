import mock

import unittest

import scrapazhon

from unittest           import TestCase

from scrapazhon.request import Request

from nose.tools         import *

from mock               import patch

from mock import MagicMock

class RequestTest(unittest.TestCase):

    def setUp(self):
        self.patcher      = patch('urllib2.urlopen')
        self.urlopen_mock = self.patcher.start()
        self.urlopen_mock = self.patcher.start()
        self.code_mock    = self.patcher.start()

    def url_instance_variable_test(self):
        request_object = Request("http://www.amazon.com/appstore")
        self.assertEqual(vars(request_object), {'url': 'http://www.amazon.com/appstore'})

    @raises(Exception)
    def url_error_exception_test(self):
        request_object = Request("htwwqtp://@@@@com/appstore")
        self.assertRaises(URLError, request_object.get_html_from_url())

    @raises(Exception)
    def http_error_exception_test(self):
        request = Request('http://www.amazon.com/holahellohalloczesc')
        self.assertRaises(HTTPError, request_object.get_html_from_url())

    def tearDown(self):
        self.patcher.stop()