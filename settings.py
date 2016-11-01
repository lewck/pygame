import dev.log
def init():
    global APIKEY
    APIKEY = 'ngyBtvxbC2dPQg2f8lmZMVAceGQo2q0skYZoAzkJd19wWBetJ0tTMaWO3HySt4m5'

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
                'buyprice': 100,
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
        },
        'metalzinc': {
            'title': 'Zinc',
            'required': {},
            'sellPrice': 5,
            'discovered': True,
        },
        'metalbrass': {
            'title': 'Brass',
            'required' : {
                'metalcopper':1,
                'metalzinc':1,
            },
            'sellPrice': 5,
            'discovered': True,
        },

        'brassnails': {
            'title': 'Brass Nails',
            'required': {
                'metalbrass':1,
                'metalzinc':1,
            },
            'sellPrice': 20,
            'discovered': False,
            'unlockPrice': 500,
        },

        'brassdagger': {
            'title': 'Brass Dragger',
            'required': {
                'metalbrass': 3,
            },
            'sellPrice': 30,
            'discovered': False,
            'unlockPrice': 1000,
        }

    }

    default_speed_upgrade = {
        1: 100,
        2: 500,
        3: 1000,
        4: 2500,
        5: 10000
    }

    default_speed_modifier = {
        0: 1,
        1: 1.1,
        2: 1.5,
        3: 2,
        4: 2.5,
        5: 3,
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
        'menumarketstatus': False,
        'menuunlock': False,
    }

    global mod
    mod = 0

    global marketCache
    marketCache = {}

    global zoom
    zoom = 10