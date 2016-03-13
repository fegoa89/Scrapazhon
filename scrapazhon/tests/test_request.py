import unittest

import scrapazhon

from unittest           import TestCase

from scrapazhon.request import Request

class URLErrorException(Exception): "urlopen error unknown url type: htwwqtp"

class RequestTest(unittest.TestCase):

    def url_instance_variable_test(self):
        requestObject = Request("http://www.amazon.com/appstore")
        self.assertEqual(vars(requestObject), {'url': 'http://www.amazon.com/appstore'})

if __name__ == "__main__":
    unittest.main()