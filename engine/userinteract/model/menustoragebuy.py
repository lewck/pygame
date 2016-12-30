from engine.userinteract.model.base import base

import settings

class menustoragebuy(base):
    def __init__(self, **kwargs):
        self.basePriority = 100
        self.basePos = [0, 0]
        self.baseDim = [512, 512]

        base.__init__(self, **kwargs)

    #--------------------------------------------------
    #  Assign Inputs
    #--------------------------------------------------
    def addInputs(self):
        self.addCommon(uid='coverall', color=(51, 51, 51))

        self.addInput(type='mouseAction', priority=9, title='close', attribute={
            'click': 1,
            'pos': [0,502],
            'dim': [100, 100],
            'event': 'close'
        })

    #--------------------------------------------------
    #  Assign Outputs
    #--------------------------------------------------
    def addOutputs(self):
        # UI
        self.addOutput(pos=[10, 10], type='text', priority=2, attribute={
            'font': 'primaryFont',
            'size': 50,
            'value': 'Storage Shop',
            'color': (255, 255, 255)
        })
        self.addOutput(pos=[0, 502], type='shape', priority=6, attribute={
            'shape': 'rectangle',
            'dim': [10, 10],
            'color': (255, 0,0)
        })


        max = len(settings.objectDB['storage'])-1
        count = 0
        posx = 12
        posy = 100

        for y in range(0,8):
            for x in range(0,12):
                self.addOutput(pos=[posy + 2, posx + 2], type='shape', priority=5, attribute={
                    'shape': 'rectangle',
                    'dim': [39, 39],
                    'color': (0, 0, 0)
                })

                if(count<=max):
                    uid = list(settings.objectDB['storage'].keys())[count]
                    self.addOutput(pos=[posy + 2, posx + 2], type='image', priority=6, attribute={
                        'uid': uid,
                        'scale': (39,39)
                    })
                    self.addInput(type='mouseclick', priority=6, attribute={
                        'click': 1,
                        'pos': [posy + 2, posx + 2],
                        'dim': [39,39],
                        'event': 'buyObject',
                        'eventArgs': ['storage','genericHouse'],
                    })
                    count += 1
                posx += 41
            posx = 12
            posy += 41
