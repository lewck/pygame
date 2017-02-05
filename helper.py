
# Commonly used functions

class helper:

    @staticmethod
    def directionToPosition(pos, direction):
        # Convert UP to DOWN, LEFT to RIGHT. Used for finding the interaction position (position which a neighbour
        # would face to interact with it).

        modifier = {
            0: -1,
            1: 1,
            2: 1,
            3: -1
        }
        if (direction == 0 or direction == 2):
            # Y direction change
            pos[0] += modifier(direction)
        if (direction == 1 or direction == 3):
            # X direction change
            pos[1] += modifier(direction)