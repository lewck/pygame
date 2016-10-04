class ioobject():
    def __init__(self, **kwargs):
        self.attribute = {}
        for key, value in kwargs.items():
            setattr(self, key, value)

    def addAttrs(self, attrs):
        for key, value in attrs.items():
            self.attribute[key] = value