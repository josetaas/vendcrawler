# Skeleton of a CLI

import click

import vendcrawler
from vendcrawler.scripts.vendcrawler import VendCrawler


@click.command('vendcrawler')
@click.argument('user')
@click.argument('password')
@click.argument('database')
@click.argument('interval')
def cli(user, password, database, interval):
    VendCrawler(user, password, database).run(interval)
