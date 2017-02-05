from webinteract.base import base
import settings


class game(base):
    def __init__(self):
        # Init parent
        super(game, self).__init__()

    def create(self, goalID, goalArgs):
        # Call 'creategame' request to web server
        request = self.requestCall('creategame', {'goal_id': goalID, 'goal_args': goalArgs})

        if(request):
            # Save response variables to global
            settings.gameData['session_id'] = request['session_id']
            settings.gameData['game_id'] = request['game_id']
            settings.gameData['game_pin'] = request['game_pin']
            settings.gameData['objectives'] = request['objectives']
            return True

        return False

    def join(self, gameID, gamePin):
        # Call 'joingame' request to web server
        request = self.requestCall('joingame', {'game_id': gameID, 'game_pin': gamePin})

        if(request):
            # Save response variables to global
            settings.gameData['session_id'] = request['session_id']
            settings.gameData['game_id'] = gameID
            settings.gameData['game_pin'] = gamePin
            settings.gameData['objectives'] = request['objectives']
            return True

        return False

    def markCompleted(self, gameID, sessionID):
        # Send the 'completeGame' command to the server, telling the game is complete
        request = self.requestCall('completeGame', {'game_id': gameID, 'session_id': sessionID})

    def checkCompleted(self):
        # Call 'checkGameComplete' request to web server
        request = self.requestCall('checkGameComplete', {'game_id': settings.gameData['game_id']})

        # Analyse response
        if(request['success'] == 1500):
            # Not completed do nothing
            return True


        # Game is Completed, update winstatus and change screen for user
        settings.winStatus = False
        settings.currentScreen = 'gameCompleted'