from engine.userinteract.model.base import base
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.helper import helper as uihelper
from webinteract.market import market
from shop import shop

import settings

class menuunlock(base):
    def __init__(self, **kwargs):
        self.basePriority = 80
        self.title = 'menuunlock'
        super(menuunlock, self).__init__(**kwargs)

    def addInputs(self):
        self.addCommon(uid='close', pos=[0, 512])

    def unlockItem(self, itemID):
        if(shop.canPurchase(settings.itemDB[itemID]['unlockPrice'])):
            shop.purchase(settings.itemDB[itemID]['unlockPrice'])
            settings.itemDB[itemID]['discovered'] = True

            uihelper.reloadModel(settings.activeModelDB[settings.activeUI['factorypartsselectpart']].id)
            uihelper.reloadModel(settings.activeModelDB[settings.activeUI['menuunlock']].id)
            uihelper.toggleModel('menuunlock')


    def addOutputs(self):
        self.addOutput(pos=[0, 0], type='shape', priority=0, title='factoryPartBackground',
           attribute={
               'shape': 'rectangle',
               'dim': [512, 512],
               'color': (0, 0, 0)
           }
        )

        self.addOutput(pos=[10, 10], type='text', priority= 2, title='factoryparttitle',
            attribute={
               'font': 'primaryFont',
               'size': 50,
               'value': 'Unlock Menu',
               'color': (255, 255, 255)
           }
        )



        basey = 50
        for key, each in settings.itemDB.items():
            if(each['discovered'] == False):
                self.addOutput(pos=[basey, 10], type='text', priority=2, title='factoryparttitle',
                   attribute={
                       'font': 'primaryFont',
                       'size': 30,
                       'value': str(each['title']) + '   Price: ' + str(each['unlockPrice']),
                       'color': (255,0,0)
                   }
                )
                self.addOutput(pos=[basey, 400], type='shape', priority= 2,
                               title='overlayBackground',
                               attribute={
                                   'shape': 'rectangle',
                                   'dim': [50, 50],
                                   'color': (255, 255, 0)
                               }
                               )
                self.addOutput(pos=[basey, 400], type='text', priority= 5,
                               title='menustoragebuytext',
                               attribute={
                                   'font': 'primaryFont',
                                   'size': 20,
                                   'value': 'Buy',
                                   'color': (0, 0, 0)
                               }
                               )

                self.addInput(type='mouseAction', priority=5, title='openmarketmenu', attribute={
                    'click': 1,
                    'pos': [basey, 400],
                    'dim': [50, 50],
                    'event': 'unlockItem',
                    'eventArgs': [str(key)],
                })



                basey += 50
        '''
        marketResponse = market()
        basey = 50
        limit = 10
        current = 0

        for each in marketResponse.get():
            if(current <= limit):
                settings.marketCache[each['itemid']] = each['current_demand']

                self.addOutput(pos=[basey, 10], type='text', priority=2, title='factoryparttitle',
                   attribute={
                       'font': 'primaryFont',
                       'size': 30,
                       'value': str(each['itemid']) + ' : ' + str(each['current_demand']),
                       'color': (255, 255, 255)
                   }
                )
                current += 1
                basey += 30
            else:
                break

            '''

    def load(self, pos):
        self.objectPosition = pos

        self.refresh()