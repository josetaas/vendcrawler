import os
import os.path
import urllib.request
from json import dumps
from multiprocessing.dummy import Pool as ThreadPool
from re import search
from time import sleep, strftime

import vendcrawler
from vendcrawler.scripts.vendpageparser import VendPageParser

class VendCrawler(object):

    def run(self, interval):
        while (True):
            link = 'https://sarahserver.net/?module=vendor'
            req = urllib.request.Request(link, headers={'User-Agent': 
                                                        'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                page_count = self.get_page_count(response.read().decode('utf-8'))
        
            links = self.get_links(int(page_count))
            pool = ThreadPool(4)
            results = pool.map(self.parse_link, links)
            pool.close()
            pool.join()
            self.save(dumps(results))
            sleep(float(interval))

    def parse_link(self, link):
        vendpageparser = VendPageParser()
        req = urllib.request.Request(link, headers={'User-Agent': 
                                                    'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            vendpageparser.feed(response.read().decode('utf-8'))

        return vendpageparser.items


    def get_links(self, page_count):
        links = []
        for x in range(1, page_count + 1):
            links.append('https://sarahserver.net/?module=vendor&p=' + str(x))
        return links

    def get_page_count(self, html):
        m = search('Found a total of (.*) record\(s\) across (.*) page', html)
        return m.group(2)

    def save(self, json):
        vc_dir = os.path.join(os.path.expanduser('~'), '.vendcrawler')
        if (not os.path.isdir(vc_dir)):
            os.mkdir(vc_dir)

        json_file = strftime('%Y-%m-%d_%H:%M:%S') + '.json'
        json_file = os.path.join(vc_dir, json_file)
        with open(json_file, 'w') as f:
            f.write(json)
