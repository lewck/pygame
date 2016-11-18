from webinteract.base import base
import settings


class game(base):
    def __init__(self):
        #Init parent
        super(game, self).__init__()

    def create(self):
        request = self.requestCall('creategame', {'goal_id': 1, 'goal_args': 50000})

        settings.gameData['session_id'] = request['session_id']
        settings.gameData['game_id'] = request['game_id']
        settings.gameData['game_pin'] = request['game_pin']

        return True

