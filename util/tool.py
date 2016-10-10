from random import randint
import string
import operator


class tool:
    @staticmethod
    def genRandomString(len=20):
        val = ''
        for i in range(len):
            val += str(randint(0,9))
        return val

    @staticmethod
    def bubbleSort(**kwargs):
        if('localvariable' in kwargs):
            if(type(kwargs['values']) is list):
                #Sort array, return array
                order = []
                for i in range(0, len(kwargs['values'])):
                    order.append(getattr(kwargs['values'][i], kwargs['localvariable']))

                for i in range(0, len(order) -1):
                    for j in range(0, len(order)-i-1):
                        if order[j] > order[j+1]:
                            buffer = order[j]
                            bufferObject = kwargs['values'][j]
                            order[j] = order[j+1]
                            kwargs['values'][j] = kwargs['values'][j + 1]
                            order[j+1] = buffer
                            kwargs['values'][j + 1] = bufferObject

            elif (type(kwargs['values']) is dict):
                #Sort Dictionary, return array
                toReturn = []
                for each in sorted(kwargs['values'].values(), key=operator.attrgetter(kwargs['localvariable'])):
                    toReturn.append(each)
                return toReturn


        else:
            for i in range(0, len(kwargs['values']) -1):
                for j in range(0, len(kwargs['values'])-i-1):
                    if kwargs['values'][j] > kwargs['values'][j+1]:
                        buffer = kwargs['values'][j]
                        kwargs['values'][j] = kwargs['values'][j+1]
                        kwargs['values'][j+1] = buffer

        return kwargs['values']