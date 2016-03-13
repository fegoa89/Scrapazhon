import unittest

import scrapazhon

from unittest           import TestCase

from scrapazhon.request import Request

from nose.tools import *

import mock

class RequestTest(unittest.TestCase):

    def url_instance_variable_test(self):
        requestObject = Request("http://www.amazon.com/appstore")
        self.assertEqual(vars(requestObject), {'url': 'http://www.amazon.com/appstore'})

    @raises(Exception)
    def url_error_exception_test(self):
        requestObject = Request("htwwqtp://@@@@com/appstore")
        self.assertRaises(URLError, requestObject.getHtmlfromUrl())

    @raises(Exception)
    def http_error_exception_test(self):
        request = Request('http://www.amazon.com/holahellohalloczesc')
        self.assertRaises(HTTPError, requestObject.getHtmlfromUrl())