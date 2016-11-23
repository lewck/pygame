from webinteract.base import base
import settings


class game(base):
    def __init__(self):
        #Init parent
        super(game, self).__init__()

    def create(self, goalID, goalArgs):
        request = self.requestCall('creategame', {'goal_id': goalID, 'goal_args': goalArgs})

        settings.gameData['session_id'] = request['session_id']
        settings.gameData['game_id'] = request['game_id']
        settings.gameData['game_pin'] = request['game_pin']
        settings.gameData['objectives'] = request['objectives']
        return True

    def join(self, gameID, gamePin):
        request = self.requestCall('joingame', {'game_id': gameID, 'game_pin': gamePin})

        settings.gameData['session_id'] = request['session_id']
        settings.gameData['game_id'] = gamePin
        settings.gameData['game_pin'] = gameID
        settings.gameData['objectives'] = request['objectives']

        return True