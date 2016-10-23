import settings

class base:
    def __init__(self):
        self.input = []
        self.output = []

        self.addInputs()
        self.addOutputs()

        self.interfaces = {'inputs': [], 'outputs': []}

    def addInput(self, **kwargs):
        #Register with event
        self.input.append(kwargs)

    def addOutput(self, **kwargs):
        #Register with event
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

    def deleteModel(self):
        #Remove Output Interface
        self.deleteInterface('output', 'all')
        # Remove Input Interface
        self.deleteInterface('input', 'all')


    def close(self):
        # Clear interfaces
        self.deleteModel()

    def none(self):
        #Called with cover-all inputs
        pass