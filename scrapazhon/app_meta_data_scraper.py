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

    def collectMetaData(self):
        metaDataDictionary = {}
        metaDataDictionary["appId"] = self.appId()
        metaDataDictionary["appName"] = self.appName()
        metaDataDictionary["appIcon"] = self.appIcon()
        metaDataDictionary["screenshots"] = self.screenshots()
        metaDataDictionary["categoriesId"] = self.categoriesId()
        metaDataDictionary["keywords"] = self.keywords()
        metaDataDictionary["price"] = self.price()
        metaDataDictionary["appPublisherName"] = self.appPublisherName()
        metaDataDictionary["customerReviewsCount"] = self.customerReviewsCount()
        metaDataDictionary["averageCustomerReview"] = self.averageCustomerReview()
        metaDataDictionary["latestUpdateDate"] = self.getAppDate("latest_developer_update")
        metaDataDictionary["releaseDate"] = self.getAppDate("original_release_date")
        metaDataDictionary["ratedOnCategory"] = self.ratedOnCategory()
        pprint.pprint(metaDataDictionary)

    def appId(self):
        return self.soupObject().find("link", rel="canonical")["href"].split("/dp/")[1]

    def appName(self):
        return self.soupObject().find("span", {"id":"btAsinTitle"}).get_text()

    def appIcon(self):
        return self.soupObject().find("img", {"id":"js-masrw-main-image"})["src"]

    def screenshots(self):
        screenshots         = []
        screenshotsArray = self.soupObject().find("ol", {"class":"a-carousel", "role":"list"}).findAll('li')
        for screenshot in screenshotsArray:
            # image src in source code contains an '._SL160_' string on the name :
            # (http://ecx.images-amazon.com/images/I/714RlrJ3iyL._SL160_.png)
            # it represents the small preview of the screenshot, without it shows
            # the original size of the screenshot
            screenshots.append(screenshot.find("img", {"class":"masrw-thumbnail"})["src"].replace("._SL160_",""))

        return screenshots

    def categoriesId(self):
        categories = []
        categoryBreadcrumb = self.soupObject().find("div", {"id":"wayfinding-breadcrumbs_feature_div"}).findAll('li')
        for category in categoryBreadcrumb:
            anchorCategoryElement = category.find_all("a", {"class":"a-link-normal a-color-tertiary"})
            if len(anchorCategoryElement) > 0:
                # The category id's that this app belongs to is defined in the link 
                # of the breadcrumb.
                categories.append(int(anchorCategoryElement[0]["href"].split("node=")[1]))

        return categories

    def keywords(self):
        return self.soupObject().find("meta", {"name":"keywords"})["content"].split(",")

    def price(self):
        return self.soupObject().find("span", {"id":"actualPriceValue"}).get_text().strip()

    def appPublisherName(self):
        return self.soupObject().find("div", {"class":"buying"}).find("a").get_text()

    def customerReviewsCount(self):
        reviewCount = self.soupObject().find("span", { "class":"dpAppstore%s" % (self.appId()) })
        # Strip and replace string
        reviewCountNumber = reviewCount.find("span", {"class":"a-size-small"}).get_text().replace(" customer reviews","").strip()
        # return as an integer
        return int(reviewCountNumber.replace(",",""))

    def averageCustomerReview(self):
        reviewAverage = self.soupObject().find("span", { "class":"dpAppstore%s" % (self.appId()) })
        reviewAverageNumber = reviewAverage.find("a", {"class":"a-link-normal a-text-normal"}).get_text().replace(" out of 5 stars","").strip()
        return float(reviewAverageNumber)

    def getAppDate(self, dateFieldKey):
        try:
            date = self.productDetailsTable()[dateFieldKey]
            time_struct, parse_status = parsedatetime.Calendar().parse(date)
            if parse_status:
                return datetime.fromtimestamp(mktime(time_struct))
        except TypeError:
            print("Can not parse %s" % dateFieldKey)

    def productDetailsTable(self):
        detailsList = self.soupObject().find("table", {"id":"productDetailsTable"}).find_all('li')
        dicDetailsResult = {}
        for detail in detailsList:
            try:
                liElement = detail.get_text().split(":")
                dictKey = liElement[0].strip().lower().replace(" ", "_")
                dicDetailsResult[dictKey] = liElement[1::1][0].strip()
            except IndexError:
                pass

        return dicDetailsResult

    def ratedOnCategory(self):
        return self.soupObject().find("span", {"id":"mas_product_rating_defintions"}).get_text().strip()

    def soupObject(self):
        soup = BeautifulSoup(self.rawHtml, "lxml")
        return soup