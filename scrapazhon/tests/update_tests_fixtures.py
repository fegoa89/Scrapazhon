import json
import os
import scrapazhon
from   scrapazhon.request import Request

mainPageHtmlResponse = Request("http://www.amazon.com/appstore").getHtmlFromUrl()

with open('scrapazhon/tests/integration/fixtures/main_page_html_response.json', 'w') as outfile:
    json.dump(mainPageHtmlResponse, outfile)