from scrapazhon import *
# Create an object of Scraper class & call a method of it

response = Request("http://www.amazon.com/appstore").getHtmlfromUrl()

HtmlParser(response).mainPageApps()