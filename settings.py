import dev.log
def init():
    global APIKEY
    APIKEY = 'ngyBtvxbC2dPQg2f8lmZMVAceGQo2q0skYZoAzkJd19wWBetJ0tTMaWO3HySt4m5'

    global zoom
    zoom = 0
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

    global itemDB
    itemDB={

        'body': {
            'title': 'body',
            'required' : {},
            'sellPrice': 50,
        },

        'plane':{
            'title': 'Plane',
            'required' : {
                'body':2,
            },
            'sellPrice': 500,
        }
    }
    global objectDB
    objectDB = {
        'placeholder': {
            'empty': {
                'title': 'empty',
                'tickListen': []
            }
        },
        'storage': {
            'genericHouse': {
                'title': 'genericHouse',
                'tickListen': []
            },
        },
        'storageVehicles': {
            'garage': {
                'title': 'garage',
                'tickListen': []
            },
        },
        'producer': {
            'factory_parts': {
                'title': 'factory_parts',
                'tickListen': [1, 10],
                'price': 100,
            },
        },
        'transport': {
            'road': {
                'title': 'road',
                'tickListen': []
            },
        },
        'exports': {
            'exports': {
                'title': 'exports',
                'tickListen': []
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
    }

    global mod
    mod = 0