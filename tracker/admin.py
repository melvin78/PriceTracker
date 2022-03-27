from categories.models import Categories
from phoneplace.admin import ScrapPhoneplace, new_data_phoneplace
from subcategory.models import SubCategory
from termcolor import colored
from colorama import init
init()

def compare_phoneplace():
        dataset_phoneplace = Categories.objects.filter(website_id=2).values('link', 'idcategories')

        website_prices = []
        database_prices = ScrapPhoneplace().allPrices()

        for values in dataset_phoneplace:
            website_prices.append(ScrapPhoneplace().trackprice(values['link']['link']))

        for item_web in website_prices[0]:
            res_db = next((item_database for item_database in database_prices if item_database['name'] == item_web['name']),
                          False)

            if res_db:
                if res_db['current_price'] > item_web['price']:
                    new_data_phoneplace().update_db(item_web['name'], item_web['price'])
                    pricedrop = float(res_db['current_price']) - float(item_web['price'])
                    print(colored(item_web['name'], 'blue') + ' was priced at ' +
                        colored(res_db['current_price'], 'magenta') + ' its now priced at ' +
                        colored(item_web['price'],'cyan') + ' a price drop of ' + colored(pricedrop,'green'))
            else:
                ids = Categories.objects.filter(category_name__icontains=item_web['name'].split()[0]).values('idcategories')
                ins = SubCategory(
                    category_id=ids,
                    name=item_web['name'],
                    current_price=item_web['price'],
                    link=item_web['link']

                )
                ins.save()
