from jobset.base import base

'''
'   Required Params:
'   position, item(id)
'''

class waitForItems(base):
    def __init__(self, **kwargs):
        self.tickListen = [10]
        super(waitForItems, self).__init__(**kwargs)
        self.pos = kwargs['position']
        self.items = kwargs['items']

    def task(self):
        pass

    def needsItem(self, itemID):
        for id, qty in self.items.items():
            if(id==itemID):
                return True
        return False