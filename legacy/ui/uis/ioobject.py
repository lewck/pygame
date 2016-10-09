
class ioobject():
    def __init__(self, **kwargs):
        self.attribute = {}
        print('kw')
        print(kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def addAttrs(self, attrs):
        for key, value in attrs.items():
            self.attribute[key] = value

    def event(self, eid):
        print('running event')
        eval(self.parent+'(event+eid)')