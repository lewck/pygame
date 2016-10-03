from random import randint
import string


class tool:
    @staticmethod
    def genRandomString(len=20):
        val = ''
        for i in range(len):
            val += str(randint(0,9))
        return val