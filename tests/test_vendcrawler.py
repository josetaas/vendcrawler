import unittest

from vendcrawler.scripts.vendcrawler import VendCrawler

class TestVendCrawlerMethods(unittest.TestCase):

    def test_get_links(self):
        links = VendCrawler().get_links(2)
        self.assertEqual(links, 
                         ['https://sarahserver.net/?module=vendor&p=1',
                          'https://sarahserver.net/?module=vendor&p=2'])

    def test_get_page_count(self):
        with open('test_vendcrawler.html', 'r') as f:
            data = f.read()
        page_count = VendCrawler().get_page_count(str(data))
        self.assertEqual(int(page_count), 84)

if __name__ == '__main__':
    unittest.main()
