import json
import os
import scrapazhon
from   scrapazhon.request import Request

# Uncomment to update the test fixtures
#app_page_html_response = Request("http://www.amazon.com/dp/B018IKM114").get_html_from_url()

#with open('scrapazhon/tests/integration/fixtures/app_page_html_response.json', 'w') as outfile:
#    json.dump(app_page_html_response, outfile)


#main_page_html_response = Request("http://www.amazon.com/appstore").get_html_from_url()

#with open('scrapazhon/tests/integration/fixtures/main_page_html_response.json', 'w') as outfile:
#    json.dump(main_page_html_response, outfile)