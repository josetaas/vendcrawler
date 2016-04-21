# Skeleton of a CLI

import click

import vendcrawler
from vendcrawler.scripts.vendcrawler import VendCrawler


@click.command('vendcrawler')
@click.argument('interval')
def cli(interval):
    VendCrawler().run(interval)
