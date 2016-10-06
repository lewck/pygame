class helper:
    @staticmethod
    def getInputWithLeftClick(haystack):
        toreturn = []
        for each in haystack:
            if each.type=='mouseAction':
                if(each.attribute['click'] == 1):
                    toreturn.append(each)

        return toreturn