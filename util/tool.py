from random import randint
import string
import operator


class tool:
    @staticmethod
    def genRandomString(length=20):
        # Generate string with specified length from below string
        chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        val = ''
        for i in range(length):
            val += chars[randint(0,len(chars)-1)]

        return val

    @staticmethod
    def genUniqueID(current, length=16):
        # Generate random string, re-generate if key already exists in provided dict
        while True:
            randomString = tool.genRandomString(length)
            if(randomString not in current):
                break

        return randomString



    @staticmethod
    def bubbleSort(**kwargs):
        if('localvariable' in kwargs):
            # Local variable provided, sort based on that. Verify values is list
            if(type(kwargs['values']) is list):
                order = []
                if('ignoreWhenFalse' in kwargs):
                    # Filter results if ignorewhenfalse attribute for local variable is false
                    for i in range(0, len(kwargs['values'])):
                        if(getattr(kwargs['values'][i], kwargs['ignoreWhenTrue'])!=False):
                            order.append(getattr(kwargs['values'][i], kwargs['localvariable']))

                else:
                    # Ignore false falter, append all values to order array with local variable
                    for i in range(0, len(kwargs['values'])):
                        order.append(getattr(kwargs['values'][i], kwargs['localvariable']))


                for i in range(0, len(order) -1):
                    for j in range(0, len(order)-i-1):
                        if order[j] > order[j+1]:
                            # Standard bubble algorithm
                            # Current selection less than next, need to switch positions
                            buffer = order[j]
                            bufferObject = kwargs['values'][j]
                            order[j] = order[j+1]
                            kwargs['values'][j] = kwargs['values'][j + 1]
                            order[j+1] = buffer
                            kwargs['values'][j + 1] = bufferObject

            elif (type(kwargs['values']) is dict):
                # Use python's sorted function to order the dict
                toReturn = []
                for each in sorted(kwargs['values'].values(), key=operator.attrgetter(kwargs['localvariable'])):
                    toReturn.append(each)
                return toReturn

        else:
            # No local variable provided, sort based of raw value
            for i in range(0, len(kwargs['values']) -1):
                for j in range(0, len(kwargs['values'])-i-1):
                    # Standard bubble algorithm
                    if kwargs['values'][j] > kwargs['values'][j+1]:
                        # Current selection less than next, need to switch positions
                        buffer = kwargs['values'][j]
                        kwargs['values'][j] = kwargs['values'][j+1]
                        kwargs['values'][j+1] = buffer

        return kwargs['values']