from engine import event

class welcome():
    def __init__(self):
        print('inited')
        self.input = []
        self.output = []

        self.addInputs()
        self.addOutputs()

    def addInput(self, **kwargs):
        #Register with event
        self.input.append(kwargs)

    def addOutput(self, **kwargs):
        #Register with event
        self.output.append(kwargs)

    def close(self):
        self.output = []


    def addInputs(self):
        self.addInput(type='mouseAction', priority = 5, attribute={
            'click': 1,
            'pos': [0, 0],
            'dim': [200, 100],
            'event': 'close'
        })

    def addOutputs(self):
        self.addOutput(pos=[200, 200], type='text', priority=50, attribute={
            'size': 10,
            'value': 'Basic introduction!',
            'color': (255, 255, 0)
        })
