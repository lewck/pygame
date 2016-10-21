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

import settings
settings.init()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 10000))


try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print('sending "%s"'+message)
    s.sendall(str.encode(message))

    # Look for the response




finally:
    while True:
        data = s.recv(16)
        if data:
            print('received "%s"' + str(data))
        else:
            print('Closing')
            break

    print ('closing socket')
    s.close()

print(s)


