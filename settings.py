import dev.log
def init():
    global APIKEY
    APIKEY = 'ngyBtvxbC2dPQg2f8lmZMVAceGQo2q0s'

    global grid
    grid = []
    global xMax
    xMax = 15
    global yMax
    yMax = 10
    global surface
    surface = 0
    global log
    log = False
    global logObject
    logObject = 0
    global devfont
    devfont = 0

    global pathDB
    pathDB = {}

    global activeEntityDB
    activeEntityDB = {}

    global activeJobDB
    activeJobDB = {}

    global activeJobsetDB
    activeJobsetDB = {}

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

    global activeInputDB
    activeInputDB = []

    global fonts
    fonts = 0

    global color
    color = {
        'white':(0,0,0),
        'red': (255,0,0)
    }

    global activeEventDB
    activeEventDB = {}

    global activeModelDB
    activeModelDB = {}

    global activeOutDB
    activeOutDB = {}

    global eventBuffer
    eventBuffer = True

    global inputBuffer
    inputBuffer = []

    global entityDB
    entityDB = {
        'vehicle': {
            'car':{
                'title': 'car',
                'buyprice': 500,
            },
            'van': {
                'title': 'van',
                'buyprice': 1000,
            },
            'lorry': {
                'title': 'lorry',
                'buyprice': 5000,
            }
        }
    }

    global itemDB
    itemDB={
        'metalcopper':{
            'title': 'Copper',
            'required': {},
            'sellPrice': 5,
            'discovered': True,
            'makes': 1,
        },
        'metalzinc': {
            'title': 'Zinc',
            'required': {},
            'sellPrice': 5,
            'discovered': True,
            'makes': 1,
        },
        'metaltin': {
            'title': 'Tin',
            'required': {},
            'sellPrice': 5,
            'discovered': True,
            'makes': 1,
        },

        'metalbronze': {
            'title': 'Bronze',
            'required' : {
                'metalcopper':1,
                'metaltin':1,
            },
            'sellPrice': 5,
            'discovered': True,
            'makes': 1,
        },

        'metalbrass': {
            'title': 'Brass',
            'required' : {
                'metalcopper':1,
                'metalzinc':1,
            },
            'sellPrice': 10,
            'discovered': True,
            'makes': 2,
        },

        'brassnails': {
            'title': 'Brass Nails',
            'required': {
                'metalbrass':1,
            },
            'sellPrice': 15,
            'discovered': False,
            'unlockPrice': 500,
            'makes': 1,
        },
        'bronzecoin': {
            'title': 'Bronze Coin',
            'required': {
                'metalbronze': 1,
            },
            'sellPrice': 15,
            'discovered': False,
            'unlockPrice': 500,
            'makes': 1,
        },

        'brassdagger': {
            'title': 'Brass Dragger',
            'required': {
                'metalbrass': 2,
            },
            'sellPrice': 30,
            'discovered': False,
            'unlockPrice': 1000,
            'makes': 1,
        }

    }

    default_speed_upgrade = {
        1: 100,
        2: 1000,
        2: 10000,
    }

    default_speed_modifier = {
        0: 1,
        1: 2,
        2: 3,
    }

    global objectDB
    objectDB = {
        'placeholder': {
            'empty': {
                'title': 'empty',
                'tickListen': [],
                'discovered': False,
            }
        },
        'storage': {
            'genericHouse': {
                'title': 'genericHouse',
                'tickListen': [],
                'discovered': False,
            },
        },
        'storageVehicles': {
            'garage': {
                'title': 'garage',
                'tickListen': [],
                'discovered': True,
            },
        },
        'producer': {
            'factory_parts': {
                'title': 'factory_parts',
                'tickListen': [1, 10],
                'price': 100,
                'discovered': True,
                'speed_upgrades': default_speed_upgrade,
                'speed_upgrades_modifier': default_speed_modifier
            },
        },
        'transport': {
            'road': {
                'title': 'road',
                'tickListen': [],
                'discovered': True,
            },
        },
        'exports': {
            'exports': {
                'title': 'exports',
                'tickListen': [5],
                'discovered': True,
            },
        },
    }

    global activeUI
    activeUI = {
        'menuproducerbuy': False,
        'menustoragebuy': False,
        'defaultoverlay': False,
        'factorypartsmenu': False,
        'factorypartsselectpart': False,
        'menuvehiclebuy': False,
        'menuunlock': False,
        'menustart': False,
        'menustartonlinegame': False,
        'menuloading': False,
    }

    global gameExcluseUI
    gameExcluseUI = {
        'menumarketstatus': False,
    }

    global mod
    mod = 0

    global marketCache
    marketCache = {}

    global zoom
    zoom = 10

    global gameData
    gameData = {'session_id':1, 'game_id':2, 'game_pin':3}