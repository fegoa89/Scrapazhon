import bs4

import scrapazhon

from bs4                    import BeautifulSoup

from scrapazhon.request     import Request

from scrapazhon.html_parser import HtmlParser


response = Request("http://www.amazon.com/appstore").getHtmlfromUrl()

HtmlParser(response).mainPageApps()