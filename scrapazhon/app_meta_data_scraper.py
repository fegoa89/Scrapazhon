from bs4 import BeautifulSoup

import time

import pprint

import parsedatetime

from datetime import datetime
from time     import mktime

class AppMetaDataScraper:
    def __init__(self, raw_html):
        self.raw_html = raw_html

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
        meta_data_dictionary["app_description"] = self.app_description()
        meta_data_dictionary["in_app_purchases"] = self.in_app_purchases()

        return meta_data_dictionary

    def app_id(self):
        return self.soup_object().find("link", rel="canonical")["href"].split("/dp/")[1]

    def app_name(self):
        return self.soup_object().find("span", {"id":"btAsinTitle"}).get_text()

    def app_icon(self):
        return self.soup_object().find("img", {"id":"js-masrw-main-image"})["src"]

    def screenshots(self):
        screenshots         = []
        screenshots_array = self.soup_object().find("ol", {"class":"a-carousel", "role":"list"}).findAll('li')
        for screenshot in screenshots_array:
            # image src in source code contains an '._SL160_' string on the name :
            # (http://ecx.images-amazon.com/images/I/714RlrJ3iyL._SL160_.png)
            # it represents the small preview of the screenshot, without it shows
            # the original size of the screenshot
            screenshots.append(screenshot.find("img", {"class":"masrw-thumbnail"})["src"].replace("._SL160_",""))

        return screenshots

    def categories_id(self):
        categories = []
        category_breadcrumb = self.soup_object().find("div", {"id":"wayfinding-breadcrumbs_feature_div"}).findAll('li')
        for category in category_breadcrumb:
            anchor_category_element = category.find_all("a", {"class":"a-link-normal a-color-tertiary"})
            if len(anchor_category_element) > 0:
                # The category id's that this app belongs to is defined in the link 
                # of the breadcrumb.
                categories.append(int(anchor_category_element[0]["href"].split("node=")[1]))

        return categories

    def keywords(self):
        return self.soup_object().find("meta", {"name":"keywords"})["content"].split(",")

    def price(self):
        app_price = self.soup_object().find("span", {"id":"actualPriceValue"})
        if app_price is not None:
            return app_price.get_text().strip()
        else:
            return "Free"

    def app_publisher_name(self):
        return self.soup_object().find("div", {"class":"buying"}).find("a").get_text()

    def customer_reviews_count(self):
        review_count = self.soup_object().find("span", { "class":"dpAppstore%s" % (self.app_id()) })
        # Strip and replace string
        review_count_number = review_count.find("span", {"class":"a-size-small"}).get_text().replace(" customer reviews","").replace(" customer review","").strip()
        # return as an integer
        return int(review_count_number.replace(",",""))

    def average_customer_review(self):
        review_average = self.soup_object().find("span", { "class":"dpAppstore%s" % (self.app_id()) })
        review_average_number = review_average.find("a", {"class":"a-link-normal a-text-normal"}).get_text().replace(" out of 5 stars","").strip()
        return float(review_average_number)

    def get_app_date(self, date_field_key):
        try:
            date = self.product_details_table()[date_field_key]
            time_struct, parse_status = parsedatetime.Calendar().parse(date)
            if parse_status:
                return datetime.fromtimestamp(mktime(time_struct))
        except TypeError:
            print("Can not parse %s" % date_field_key)

    def product_details_table(self):
        details_list = self.soup_object().find("table", {"id":"productDetailsTable"}).find_all('li')
        dic_details_result = {}
        for detail in details_list:
            try:
                li_element = detail.get_text().split(":")
                dict_key = li_element[0].strip().lower().replace(" ", "_")
                dic_details_result[dict_key] = li_element[1::1][0].strip()
            except IndexError:
                pass

        return dic_details_result

    def rated_on_category(self):
        return self.soup_object().find("span", {"id":"mas_product_rating_defintions"}).get_text().strip()

    def product_features(self):
        details_list = self.soup_object().find("div", {"id":"feature-bullets-btf"}).find_all('li')
        details_result_array = []
        for detail in details_list:
            try:
                details_result_array.append(detail.get_text())
            except IndexError:
                pass

        return details_result_array

    def app_description(self):
        description = self.soup_object().find("div", {"id":"mas-product-description"}).find("div", {"class":"a-row masrw-content-row"}).get_text().strip()
        return description

    def in_app_purchases(self):
        in_app_purchases = self.soup_object().find("span", {"id":"offer_inapp_popover"})

        if in_app_purchases is not None:
            return True
        else:
            return False

    def soup_object(self):
        soup = BeautifulSoup(self.raw_html, "lxml")
        return soup