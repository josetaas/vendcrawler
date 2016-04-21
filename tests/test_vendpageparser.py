import unittest

from vendcrawler.scripts.vendpageparser import VendPageParser

class TestVendPageParserMethods(unittest.TestCase):

    def test_feed(self):
        with open('test_vendcrawler.html', 'r') as f:
            data = f.read()
        vendpageparser = VendPageParser()
        vendpageparser.feed(str(data))
        self.assertEqual(vendpageparser.items[0]['id'], '2221')
        self.assertEqual(vendpageparser.items[1]['name'], 'Buckler [1]')
        self.assertEqual(vendpageparser.items[3]['amount'], '12')
        self.assertEqual(vendpageparser.items[4]['vendor'], '186612')

if __name__ == '__main__':
    unittest.main()
