import settings

class inputbuffer:
    @staticmethod
    def getTitleType(title):
        # private function
        # 0 Type = Click Buffer
        # 1 Type = Key button Buffer
        titleType = {
            0: ['setObject'],
            1: ['getKeyInput']
        }
        for key, value in titleType.items():
            for each in value:
                if(each == title):
                    return key

        return False
    @staticmethod
    def get():
        return settings.inputBuffer

    @staticmethod
    def exists():
        if('type' in settings.inputBuffer):
            return True
        return False

    @staticmethod
    def create(title, **kwargs):
        '''
        for key input, args = [maxlength]

        :param title:
        :param args:
        :return:
        '''

        if(title == 'setObject'):
            # Set object specifc variables
            settings.inputBuffer['click'] = 1

        elif(title == 'getKeyInput'):
            # Text input specific variables
            settings.inputBuffer['value'] = ''
            settings.inputBuffer['trigger'] = kwargs['trigger']
            settings.inputBuffer['model'] = kwargs['model']
            settings.inputBuffer['maxlength'] = kwargs['maxlength']


        settings.inputBuffer['type'] = inputbuffer.getTitleType(title)
        settings.inputBuffer['title'] = title
        settings.inputBuffer['args'] = kwargs

    @staticmethod
    def isClick():
        if(inputbuffer.exists()):
            if(settings.inputBuffer['type'] == 0):
                return True
            return False

    @staticmethod
    def isKey():
        if (inputbuffer.exists()):
            if(settings.inputBuffer['type'] == 1):
                return True
            return False

    @staticmethod
    def clear():
        settings.inputBuffer = {}

    @staticmethod
    def getArgs():
        return settings.inputBuffer['args']

    @staticmethod
    def getClick():
        return settings.inputBuffer['click']

    @staticmethod
    def addKey(key):
        if(len(settings.inputBuffer['value']) < settings.inputBuffer['maxlength']):
            settings.inputBuffer['value'] += key

    @staticmethod
    def delKey():
        settings.inputBuffer['value'] = settings.inputBuffer['value'][:-1]
        return True

    @staticmethod
    def complete():
        if(settings.inputBuffer['type'] == 1):
            # Assume Key Input
            getattr(settings.activeModelDB[settings.inputBuffer['model']], settings.inputBuffer['trigger'])(settings.inputBuffer['value'])

        inputbuffer.clear()
