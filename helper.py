
'''
'
'   Helper functions that are used often
'
'''

class helper:
    @staticmethod
    def directionToPosition(pos, direction):
        #TODO test before implimentation
        pass
        modifier = {
            0: -1,
            1: 1,
            2: 1,
            3: -1
        }
        if (direction == 0 or direction == 2):
            #Y direction change
            pos[0] += modifier(direction)
        if (direction == 1 or direction == 3):
            #X direction change
            pos[1] += modifier(direction)