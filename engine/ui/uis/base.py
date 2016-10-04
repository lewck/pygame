class base():
    def __init__(self, **kwargs):
        self.activeOutput = []
        self.activeInput = []

        for key, value in kwargs.items():
            setattr(self, key, value)