from shop import shop
from entity.factory import factory as entity
import settings

class base:
    def __init__(self, **kwargs):
        self.input = []
        self.output = []

        self.addInputs()
        self.addOutputs()

        self.interfaces = {'inputs': [], 'outputs': []}

        self.active = False

        for key, value in kwargs.items():
            setattr(self, key, value)

    def addInput(self, **kwargs):
        #Register with event
        kwargs['priority'] += self.basePriority
        self.input.append(kwargs)

    def addOutput(self, **kwargs):
        #Register with event
        kwargs['priority'] += self.basePriority
        self.output.append(kwargs)

    def addInterfaces(self, ins, outs):
        self.interfaces['inputs'].extend(ins)
        self.interfaces['outputs'].extend(outs)

    def deleteInterface(self, type, id):
        if(type=='output'):
            toDelete = []
            if(id=='all'):
                for key, each in settings.activeOutDB.items():
                    if(each.modelID == self.id):
                        toDelete.append(key)

            else:
                del settings.activeOutDB[id]

            for each in toDelete:
                del settings.activeOutDB[each]
        elif(type=='input'):
            toDelete = []
            if(id=='all'):
                for key, each in settings.activeEventDB.items():
                    if(each.modelID == self.id):
                        toDelete.append(key)

            else:
                del settings.activeEventDB[id]

            for each in toDelete:
                del settings.activeEventDB[each]

    def closeInterface(self, type, id):

        if(type=='output'):
            toDelete = []
            if(id=='all'):
                for key, each in settings.activeOutDB.items():
                    if(each.modelID == self.id):
                        each.active = False

            else:
                settings.activeOutDB[id].active = False


        elif(type=='input'):
            toDelete = []
            if(id=='all'):
                for key, each in settings.activeEventDB.items():
                    if(each.modelID == self.id):
                        each.active = False

            else:
                settings.activeOutDB[id].active = False


    def deleteModel(self):
        #Remove Output Interface
        self.deleteInterface('output', 'all')
        # Remove Input Interface
        self.deleteInterface('input', 'all')

    def closeModel(self):
        # Remove Output Interface
        self.closeInterface('output', 'all')
        # Remove Input Interface
        self.closeInterface('input', 'all')


    def close(self):
        # Clear interfaces
        print('CLOSEING')
        self.active = False
        self.closeModel()

    def none(self):
        #Called with cover-all inputs
        pass

    def activate(self):
        self.active = True
        for key, each in settings.activeOutDB.items():
            if (each.modelID == self.id):
                each.active = True

        for key, each in settings.activeEventDB.items():
            if (each.modelID == self.id):
                each.active = True

    def reload(self):
        self.input = []
        self.output = []
        self.addInputs()
        self.addOutputs()

    def addCommon(self, **kwargs):
        #Required args: UID
        if(kwargs['uid'] == 'close'):
            #Required Args: Pos (top right model)
            self.addInput(type='mouseAction', priority=9, title='close', attribute={
                'click': 1,
                'pos': [kwargs['pos'][0], kwargs['pos'][1]-20],
                'dim': [20, 20],
                'event': 'close'
            })
            self.addOutput(pos=[kwargs['pos'][0], kwargs['pos'][1]-20], type='shape', priority=6, title='close',
               attribute={
                   'shape': 'rectangle',
                   'dim': [20, 20],
                   'color': (255, 0, 0)
            })

        if(kwargs['uid'] == 'coverall'):
            #Required Args: Pos (top right model)
            self.addInput(type='mouseAction', priority=0, title='base', attribute={
                'click': 1,
                'pos': [0,0],
                'dim': [512,512],
                'event': 'none'
            })
            self.addInput(type='mouseAction', priority=0, title='base', attribute={
                'click': 3,
                'pos': self.basePos,
                'dim': self.baseDim,
                'event': 'none'
            })

    def buyObject(self, type, uid):
        settings.inputBuffer = ['setObject', uid]
        print('ib'+str(settings.inputBuffer))
        self.close()

    def buyEntity(self, type, uid):
        price = settings.entityDB[type][uid]['buyprice']
        if(shop.canPurchase(price)):
            shop.purchase(price)
            entity.create(uid='car')
