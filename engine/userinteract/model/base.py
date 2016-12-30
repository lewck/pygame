from shop import shop
import entity
from engine.inputbuffer import inputbuffer
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

    #--------------------------------------------------
    #  Adding I/O
    #--------------------------------------------------
    # Called by model, format and append result to
    # the I/O list
    #
    def addInput(self, **kwargs):
        # Register with event, set correct priority (account for unset)
        if('priority' in kwargs):
            kwargs['priority'] += self.basePriority
        else:
            kwargs['priority'] = self.basePriority

        self.input.append(kwargs)

    def addOutput(self, **kwargs):
        # Register with event
        if ('priority' in kwargs):
            kwargs['priority'] += self.basePriority
        else:
            kwargs['priority'] = self.basePriority

        self.output.append(kwargs)

    #--------------------------------------------------
    #  Adding Interfaces
    #--------------------------------------------------
    # Called during creating, extend current I/O with
    # newly registered I/O
    #
    def addInterfaces(self, ins, outs):
        self.interfaces['inputs'].extend(ins)
        self.interfaces['outputs'].extend(outs)

    def deleteInterface(self, type):
        toDelete = []
        if(type=='output'):
            for key, each in settings.activeOutDB.items():
                if(each.modelID == self.id):
                    toDelete.append(key)
            for each in toDelete:
                del settings.activeOutDB[each]

        elif(type=='input'):
            for key, each in settings.activeEventDB.items():
                if(each.modelID == self.id):
                    toDelete.append(key)

            for each in toDelete:
                del settings.activeEventDB[each]

    #--------------------------------------------------
    #  Close Interfaces
    #--------------------------------------------------
    # Set the active state of all registered I/O to
    # False
    #
    def closeAllInterface(self, type):
        if(type=='output'):
            for key, each in settings.activeOutDB.items():
                if(each.modelID == self.id):
                    each.active = False


        elif(type=='input'):
            for key, each in settings.activeEventDB.items():
                if(each.modelID == self.id):
                    each.active = False

    def deleteModel(self):
        # Remove Output Interface
        self.deleteInterface('output', 'all')
        # Remove Input Interface
        self.deleteInterface('input', 'all')

    def closeModel(self):
        # Remove Output Interface
        self.closeAllInterface('output')
        # Remove Input Interface
        self.closeAllInterface('input')

    def close(self):
        # Deactivate self, deactivate I/O
        self.active = False
        self.closeModel()

    def none(self):
        # Called by cover-all inputs
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
        # Clear and reload I/O from model
        self.input = []
        self.output = []
        self.addInputs()
        self.addOutputs()

    def addCommon(self, **kwargs):
        # Required args: UID

        if(kwargs['uid'] == 'close'):
            # Required Args: Pos (top right model)
            self.addInput(type='mouseAction', priority=9, attribute={
                'click': 1,
                'pos': [kwargs['pos'][0], kwargs['pos'][1]-20],
                'dim': [20, 20],
                'event': 'close'
            })
            self.addOutput(pos=[kwargs['pos'][0], kwargs['pos'][1]-20], type='shape', priority=6,
               attribute={
                   'shape': 'rectangle',
                   'dim': [20, 20],
                   'color': (255, 0, 0)
            })

        if(kwargs['uid'] == 'coverall'):
            self.addInput(type='mouseAction', attribute={
                'click': 1,
                'pos': self.basePos,
                'dim': self.baseDim,
                'event': 'none'
            })
            self.addInput(type='mouseAction', attribute={
                'click': 3,
                'pos': self.basePos,
                'dim': self.baseDim,
                'event': 'none'
            })

            # Optional Args: color
            if('color' in kwargs):
                # Assume wants solid background
                self.addOutput(pos=self.basePos, type='shape', attribute={
                   'shape': 'rectangle',
                   'dim': self.baseDim,
                   'color': kwargs['color']
                })

    #--------------------------------------------------
    #  Common Model-Specific Functions
    #--------------------------------------------------
    def buyObject(self, type, uid):
        inputbuffer.create('setObject', object = uid)
        self.close()

    def buyEntity(self, type, uid):
        price = settings.entityDB[type][uid]['buyprice']
        if(shop.canPurchase(price)):
            shop.purchase(price)
            entity.factory.create(uid=uid)
