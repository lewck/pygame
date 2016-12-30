from engine.userinteract.model.base import base
import settings

class menufactorybuy(base):
    def __init__(self, **kwargs):
        self.basePriority = 120
        self.basePos = [0,0]
        self.baseDim = [512,512]

        base.__init__(self, **kwargs)

    #--------------------------------------------------
    #  Assign Inputs
    #--------------------------------------------------
    def addInputs(self):
        self.addCommon(uid='close', pos=[0,512])
        self.addCommon(uid='coverall', color=(51,51,51))

    #--------------------------------------------------
    #  Assign Outputs
    #--------------------------------------------------
    def addOutputs(self):
        # UI
        self.addOutput(pos=self.basePos, type='text', priority= 2, attribute={
            'font': 'primaryFont',
            'size': 50,
            'value': 'Producer Shop',
            'color': (255, 255, 255)
        })

        # Concatenate producers and processors
        toShow = settings.objectDB['producer']
        toShow.update(settings.objectDB['processor'])

        max = len(toShow)-1
        count = 0
        posx = 12
        posy = 100

        for y in range(0,8):
            for x in range(0,12):
                # Tile Background
                self.addOutput(pos=[posy + 2, posx + 2], type='shape', priority= 5, attribute={
                    'shape': 'rectangle',
                    'dim': [39, 39],
                    'color': (0, 0, 0)
                })

                if(count<=max):
                    # Show Item, add input
                    uid = list(toShow.keys())[count]
                    self.addOutput(pos=[posy + 2, posx + 2], type='image', priority= 6, attribute={
                        'uid': uid,
                        'scale': (39,39)
                    })

                    self.addInput(type='mouseclick', priority= 6, attribute={
                        'click': 1,
                        'pos': [posy + 2, posx + 2],
                        'dim': [39,39],
                        'event': 'buyObject',
                        'eventArgs': ['producer',uid],
                    })
                    count += 1
                posx += 41
            posx = 12
            posy += 41