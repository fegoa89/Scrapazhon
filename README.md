# Scrapazhon

Scrapes Amazon App Store with Python

> Work in progress, This package is not finalized yet.

## Update test fixtures

```python
import json
import os
import scrapazhon
from   scrapazhon.request import Request

app_page_html_response = Request("http://www.amazon.com/dp/B018IKM114").get_html_from_url()

with open('scrapazhon/tests/integration/fixtures/app_page_html_response.json', 'w') as outfile:
    json.dump(app_page_html_response, outfile)


main_page_html_response = Request("http://www.amazon.com/appstore").get_html_from_url()

with open('scrapazhon/tests/integration/fixtures/main_page_html_response.json', 'w') as outfile:
    json.dump(main_page_html_response, outfile)

```

## Main Page Scraper

Returns the list of apps that appears on amazon App Store ( "http://www.amazon.com/appstore" ). 
Each of those list is a representation of the apps that appears within each row.

```python
[{'row_label': u'Top-rated Underground Apps & Games',
'apps': [
    { 'app_icon': 'http://ecx.images-amazon.com/images/I/815yacGUJWL._SL150_.png',
      'app_id': 'B0129SZB04',
      'app_name': 'Jetpack Joyride'},
   {  'app_icon': 'http://ecx.images-amazon.com/images/I/41QyoqvrbVL._SL150_.png',
      'app_id': 'B0106IXFYS',
      'app_name': 'Flow Free'},
   {  'app_icon': 'http://ecx.images-amazon.com/images/I/81iJCheg8sL._SL150_.png',
      'app_id': 'B00YSPAXJG',
      'app_name': 'Sonic Dash'},
   {  'app_icon': 'http://ecx.images-amazon.com/images/I/81-Jz6FJDKL._SL150_.png',
      'app_id': 'B00ZQ7KONA',
      'app_name': 'Fruit Ninja'},
   {  'app_icon': 'http://ecx.images-amazon.com/images/I/81bZvPO4QtL._SL150_.png',
      'app_id': 'B01274NCT2',
      'app_name': 'Cut the Rope: Time Travel HD'},
   {  'app_icon': 'http://ecx.images-amazon.com/images/I/91unr3tmp0L._SL150_.png',
      'app_id': 'B013KNQ2MS',
      'app_name': 'Goat Simulator'},
   {  'app_icon': 'http://ecx.images-amazon.com/images/I/81Z8ArOjwQL._SL150_.png',
      'app_id': 'B00XDNH9R8',
      'app_name': 'Coin Dozer'}]
}]
```


## App Meta Data Scraper

Returns the metadata for an app .


```python
{'app_icon': 'https://images-na.ssl-images-amazon.com/images/I/6102ToQv2YL.png',
 'app_id': 'B018IKM114',
 'app_name': u'Peppa Pig: Holiday',
 'app_publisher_name': u'Entertainment One Ltd',
 'average_customer_review': 4.1,
 'categories_id': [2350149011, 9408582011, 9408584011],
 'customer_reviews_count': 45,
 'keywords': ['Peppa Pig: Holiday', 'Entertainment One Ltd'],
 'latest_update_date': datetime.datetime(2016, 2, 10, 15, 47, 35),
 'price': u'$2.99',
 'product_features': [u'5 x fun-filled games featuring Peppa, George and their family and friends:',
                      u'Take part in a swimming race',
                      u'Make a pizza with Peppa and George',
                      u'Help Aunty Goat make delicious ice-cream for everyone',
                      u'Travel through the airport',
                      u'Dress Peppa and George for the beach',
                      u"Create a postcard to capture Peppa's holiday adventure",
                      u'Singalong to the Sky High Song',
                      u'Sticker rewards'],
 'rated_on_category': u'All Ages',
 'release_date': datetime.datetime(2015, 12, 4, 15, 47, 35),
 'screenshots': ['https://images-na.ssl-images-amazon.com/images/I/714RlrJ3iyL.png',
                 'https://images-na.ssl-images-amazon.com/images/I/71uAlAW1eXL.png',
                 'https://images-na.ssl-images-amazon.com/images/I/71-Cuor98VL.png',
                 'https://images-na.ssl-images-amazon.com/images/I/71W6WGv%2BrTL.png',
                 'https://images-na.ssl-images-amazon.com/images/I/81leirTtN%2BL.png',
                 'https://images-na.ssl-images-amazon.com/images/I/719b9sf6gmL.png',
                 'https://images-na.ssl-images-amazon.com/images/I/81CjYfvk8aL.png'],
'app_description': u'Back by popular demand and relaunched for 2015. Peppa is going on holiday and she wants you to join her travels in this official app.If you have bought the app previously and download it HERE for a second time, you will be charged again.Fans of the show will love this holiday inspired adventure, which encourages them to explore the wonderful world of Peppa through interactive games and activities, featuring much loved characters, music and sound effects.No adverts, no in-app purchases, just lots of holiday fun!Please note: This app is not compatible with the iPad 1'}

```