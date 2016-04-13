# This class scrapes the MetaData for a given app:
# app id
# app name
# icon
# screenshots
# categoriesId
# Keywords
# price
# app publisher name
# customer reviews count
# app permissions
# average customer review
# version
# release date
# latest update date
# latest update comment
# rated on category
# app features
# app description
# size
# minimum operating system
# approximate download time

from bs4 import BeautifulSoup

import time

import pprint

import parsedatetime

from datetime import datetime
from time     import mktime

class AppMetaDataScraper:
    def __init__(self, raw_html):
        self.rawHtml = raw_html

    def collect_meta_data(self):
        meta_data_dictionary = {}
        meta_data_dictionary["app_id"] = self.app_id()
        meta_data_dictionary["app_name"] = self.app_name()
        meta_data_dictionary["app_icon"] = self.app_icon()
        meta_data_dictionary["screenshots"] = self.screenshots()
        meta_data_dictionary["categories_id"] = self.categories_id()
        meta_data_dictionary["keywords"] = self.keywords()
        meta_data_dictionary["price"] = self.price()
        meta_data_dictionary["app_publisher_name"] = self.app_publisher_name()
        meta_data_dictionary["customer_reviews_count"] = self.customer_reviews_count()
        meta_data_dictionary["average_customer_review"] = self.average_customer_review()
        meta_data_dictionary["latest_update_date"] = self.get_app_date("latest_developer_update")
        meta_data_dictionary["release_date"] = self.get_app_date("original_release_date")
        meta_data_dictionary["rated_on_category"] = self.rated_on_category()
        meta_data_dictionary["product_features"] = self.product_features()
        pprint.pprint(meta_data_dictionary)

    def app_id(self):
        return self.soup_object().find("link", rel="canonical")["href"].split("/dp/")[1]

    def app_name(self):
        return self.soup_object().find("span", {"id":"btAsinTitle"}).get_text()

    def app_icon(self):
        return self.soup_object().find("img", {"id":"js-masrw-main-image"})["src"]

    def screenshots(self):
        screenshots         = []
        screenshotsArray = self.soup_object().find("ol", {"class":"a-carousel", "role":"list"}).findAll('li')
        for screenshot in screenshotsArray:
            # image src in source code contains an '._SL160_' string on the name :
            # (http://ecx.images-amazon.com/images/I/714RlrJ3iyL._SL160_.png)
            # it represents the small preview of the screenshot, without it shows
            # the original size of the screenshot
            screenshots.append(screenshot.find("img", {"class":"masrw-thumbnail"})["src"].replace("._SL160_",""))

        return screenshots

    def categories_id(self):
        categories = []
        categoryBreadcrumb = self.soup_object().find("div", {"id":"wayfinding-breadcrumbs_feature_div"}).findAll('li')
        for category in categoryBreadcrumb:
            anchorCategoryElement = category.find_all("a", {"class":"a-link-normal a-color-tertiary"})
            if len(anchorCategoryElement) > 0:
                # The category id's that this app belongs to is defined in the link 
                # of the breadcrumb.
                categories.append(int(anchorCategoryElement[0]["href"].split("node=")[1]))

        return categories

    def keywords(self):
        return self.soup_object().find("meta", {"name":"keywords"})["content"].split(",")

    def price(self):
        return self.soup_object().find("span", {"id":"actualPriceValue"}).get_text().strip()

    def app_publisher_name(self):
        return self.soup_object().find("div", {"class":"buying"}).find("a").get_text()

    def customer_reviews_count(self):
        reviewCount = self.soup_object().find("span", { "class":"dpAppstore%s" % (self.app_id()) })
        # Strip and replace string
        reviewCountNumber = reviewCount.find("span", {"class":"a-size-small"}).get_text().replace(" customer reviews","").strip()
        # return as an integer
        return int(reviewCountNumber.replace(",",""))

    def average_customer_review(self):
        reviewAverage = self.soup_object().find("span", { "class":"dpAppstore%s" % (self.app_id()) })
        reviewAverageNumber = reviewAverage.find("a", {"class":"a-link-normal a-text-normal"}).get_text().replace(" out of 5 stars","").strip()
        return float(reviewAverageNumber)

    def get_app_date(self, dateFieldKey):
        try:
            date = self.product_details_table()[dateFieldKey]
            time_struct, parse_status = parsedatetime.Calendar().parse(date)
            if parse_status:
                return datetime.fromtimestamp(mktime(time_struct))
        except TypeError:
            print("Can not parse %s" % dateFieldKey)

    def product_details_table(self):
        detailsList = self.soup_object().find("table", {"id":"productDetailsTable"}).find_all('li')
        dicDetailsResult = {}
        for detail in detailsList:
            try:
                liElement = detail.get_text().split(":")
                dictKey = liElement[0].strip().lower().replace(" ", "_")
                dicDetailsResult[dictKey] = liElement[1::1][0].strip()
            except IndexError:
                pass

        return dicDetailsResult

    def rated_on_category(self):
        return self.soup_object().find("span", {"id":"mas_product_rating_defintions"}).get_text().strip()

    def product_features(self):
        detailsList = self.soup_object().find("div", {"id":"feature-bullets-btf"}).find_all('li')
        detailsResultArray = []
        for detail in detailsList:
            try:
                detailsResultArray.append(detail.get_text())
            except IndexError:
                pass

        return detailsResultArray

    def soup_object(self):
        soup = BeautifulSoup(self.rawHtml, "lxml")
        return soup