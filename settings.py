import dev.log
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
    global log
    log = False
    global logObject
    logObject = 0
    global devfont
    devfont = 0

    global pathDB
    pathDB = []

    global activeEntityDB
    activeEntityDB = {}

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
        'vegetable':{
            'vegetableCarrot':{
                'title': 'Carrot'
            }
        },

        'body': {
            'title': 'body',
            'required' : {}
        },

        'plane':{
            'title': 'Plane',
            'required' : {
                'body':2,
            }
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
            'farm_1': {
                'title': 'farm_1',
                'tickListen': [1,10],
                'price': 100,
            },
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
        }
    }

    global activeUI
    activeUI = {
        'menuproducerbuy': False,
        'menustoragebuy': False,
    }

    global mod
    mod = 0