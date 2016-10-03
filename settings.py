
def init():
    global APIKEY
    APIKEY = 'ngyBtvxbC2dPQg2f8lmZMVAceGQo2q0skYZoAzkJd19wWBetJ0tTMaWO3HySt4m5'

    global zoom
    zoom = 0
    global grid
    grid = []
    global xMax
    xMax = 10
    global yMax
    yMax = 10
    global surface
    surface = 0
    global itemIDName
    itemIDName = {
        1: ['vegetableCarrot'],
        2: ['vegetableMore']
    }
    global log
    log = False
    global logObject
    logObject = 0
    global devfont
    devfont = 0

    global pathDB
    pathDB = []

    global activeEntityDB
    activeEntityDB = []

    global activeJobDB
    activeJobDB = []

    global activeJobsetDB
    activeJobsetDB = []

    global tick
    tick = 0

    global gameExit
    gameExit = False

    global devInputBuffer
    devInputBuffer = False

    global player
    player = 0

    global activeOutputDB
    activeOutputDB = []