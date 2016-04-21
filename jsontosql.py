import os
import os.path
from json import loads

import click

from vendcrawler.scripts.vendcrawlerdb import VendCrawlerDB

class JSONToSQL(object):

    def __init__(self, json, user, password, database):
        data = loads(json.read())
        db = VendCrawlerDB(user, password, database)

        
        table = 'items'
        columns = ['item_id', 'item_name', 'vendor_id', 'shop_name',
                   'amount', 'price', 'map', 'datetime']
        values = []
        for items in data:
            for item in items:
                value = [int(item['id']),
                        item['name'],
                        int(item['vendor_id']),
                        item['shop'], 
                        int(item['amount'].replace(',', '')),
                        int(item['price'].replace(',', '')),
                        item['map'],
                        item['datetime']]

                values.append(value)

        self.db.insert(table, columns, values)


@click.command()
@click.argument('json', type=click.File('r'))
@click.argument('user')
@click.argument('password')
@click.argument('database')
def cli(json, user, password, database):
    JSONToSQL(json, user, password, database)

if __name__ == '__main__':
    cli()
