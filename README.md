# Scrapazhon
--------

Scrapes Amazon App Store with Python

> Work in progress, This package is not finalized yet.

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
