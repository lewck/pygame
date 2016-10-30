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

from inventory import inventory

import settings

settings.init()


inventoryInput = inventory(30)
inventoryOutput = inventory(30)



inventoryOutput.segregate(['metalcopper', 'metalzinc'])

inventoryOutput.addItem('metalcopper',30)
#inventoryOutput.addItem('metalzinc',40)

print(inventoryOutput.takeItem('metalcopper', 25))

if(inventoryOutput.has('metalcopper', 5)):
    print('FULL')

for each in inventoryOutput.getInventory('metalcopper'):
    print(each)