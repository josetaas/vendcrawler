from collections import OrderedDict

import vendfinder

class LinkFactory(object):
    def __init__(self):
        self.keys = OrderedDict()
        self.keys['module'] = 'vendor'
        self.keys['action'] = 'index'
        self.keys['item_id'] = ''
        self.keys['name'] = ''
        self.keys['refine_op'] = 'eq'
        self.keys['refine'] = ''
        self.keys['vendor'] = ''
        self.keys['shop'] = ''
        self.keys['price_op'] = 'eq'
        self.keys['price'] = ''
        self.keys['map'] = ''

    def create(self):
        link = 'https://sarahserver.net/?'
        first = True
        for k, v in self.keys.items():
            if not first:
                link += '&'
            link += k + '=' + str(v)
            first = False
        return link
