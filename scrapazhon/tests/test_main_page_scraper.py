import unittest

import scrapazhon

from unittest           import TestCase

from nose.tools         import *

from scrapazhon.main_page_scraper import MainPageScraper

class MainPageScraperTest(unittest.TestCase):

    def extract_app_id_from_link_test(self):
        app_id_result = MainPageScraper("").extract_app_id_from_link("/NBC-News-Digital-LLC-TODAY/dp/B00E5Q5GN6")
        self.assertEqual( app_id_result, "B00E5Q5GN6" )