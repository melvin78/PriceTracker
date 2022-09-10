<p align="center"><a href="https://cinema.webmelvin.me" target="_blank"><img src="https://cinema.webmelvin.me/popcorn.png" width="400"></a></p>

## Demo

Check out [here](https://price-tracker.webmelvin.me)

## PhonePlace Price Tracker

This is a price tracker project that scraps data from this [website](https://www.phoneplacekenya.com/) and keeps track of phone prices. Notices changes to price drops,
when a new item has been added to the store and save the records to a persistent storage, which
is then displayed in chart form. Open to contributions!
Technologies used [django](https://www.djangoproject.com/) for persisting price drops to DB, [beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
for parsing html data and [celery](https://docs.celeryq.dev/en/stable/) for running the whole process in the background.


## Features
- Shows date when the price of a phone last dropped
- Shows the highest and lowest price an item has ever peaked or dropped
- Represent all data in a chart format with the help of [apex charts](https://apexcharts.com/)

## Switch between currencies

With the help of this [api](https://api.exchangerate.host) currency conversions are done in real time
. Conversion are done between KES,USD,EUR and GBP.


Example:See screenshots below for currency conversion on the Price of Samsung Galaxy ULTRA 5G
and Apple Iphone 13 Pro Max

KES:
<img src="https://price-tracker.webmelvin.me/demo/switch-currency-one.png" alt="here">

USD
<img src="https://price-tracker.webmelvin.me/demo/switch-currency-two.png" alt="here">

## Price drop per item

You can also see the price history of each item per company brand.

See screenshots below
<img src="https://price-tracker.webmelvin.me/demo/dropdown-one.png" alt="here">

<img src="https://price-tracker.webmelvin.me/demo/dropdown-two.png" alt="here">

