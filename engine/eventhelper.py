import settings
from engine.ui.uis.popups.welcome import welcome

class eventhelper():
    @staticmethod
    def call(eventID):
        # Find Position
        for i in range(0, len(settings.activeEventDB)):
            if (settings.activeEventDB[i].id == eventID):
                settings.activeEventDB[i].doEvent()
                break
