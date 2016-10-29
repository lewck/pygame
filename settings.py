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

        'body': {
            'title': 'body',
            'required' : {},
            'sellPrice': 5,
        },

        'plane':{
            'title': 'Plane',
            'required' : {
                'body':2,
            },
            'sellPrice': 15,
        },
        'metalcopper':{
            'title': 'Copper',
            'required': {},
            'sellPrice': 5,
        },
        'metalzinc': {
            'title': 'Zinc',
            'required': {},
            'sellPrice': 5,
        },
        'metalbrass': {
            'title': 'Brass',
            'required' : {
                'metalcopper':1,
                'metalzinc':1,
            },
            'sellPrice': 5,
        },
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
                'tickListen': [5]
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
    }

    global mod
    mod = 0

    global marketCache
    marketCache = {}

    global zoom
    zoom = 10