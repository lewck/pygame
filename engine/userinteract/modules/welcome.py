from engine import event

class welcome():
    def __init__(self):
        print('inited')
        self.input = []
        self.output = []

    def addInput(self, **kwargs):
        #Register with event
        self.input.append(**kwargs)

    def addOutput(self, **kwargs):
        #Register with event
        self.output.append(**kwargs)


    def addInputs(self):

        self.addInput(type='mouseAction', priority = 5, attributes={
            'click': 1,
            'pos': [0, 0],
            'dim': [200, 100],
            'eventID': self.addEvent('close'),
        })
