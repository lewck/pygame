'''

from webinteract.score import score
import settings
settings.init()

scoreHandler = score()


scoreHandler.create('Lewis', 100)

import settings
from player.player import player
settings.init()

player = player(id='2183218e9sadasdnsaj39213', gvdifficulty = 9)

print(player.gameVariables['difficulty'])
print(player.gameVariables['balance'])

'''

from engine.userinteract.ui import ui
from engine.event import event

from webinteract.score import score
import settings

settings.init()

score = score()
score.create('Lewis', 5000)