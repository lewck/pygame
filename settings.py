import util.log

def init():
    # Used in webinteract > base.py
    # required for authentication
    global APIKEY
    APIKEY = 0


    # Used extensively
    # required for object placement
    global grid
    grid = []

    # Used in canvas setup
    # defines width and height of canvas
    global canvasDimensions
    canvasDimensions = (1050, 550)

    # Used extensively
    # required for grid dimentions
    global xMax
    xMax = 15
    global yMax
    yMax = 10

    # Used engine > render.py
    # placeholder for pygame surface
    global surface
    surface = 0

    # Used main.py
    # Current screen shown to the user
    global currentScreen
    currentScreen = 'menu'

    # Used tools > log.py
    # decides if text logging should be enabled
    global log
    log = False

    # Used extensively
    # Called to create new log line
    global logObject
    logObject = 0

    # Used in pathfind.py
    # Stores pre found paths
    global pathDB
    pathDB = {}

    # Used entity > *
    # Storage for current entities
    global activeEntityDB
    activeEntityDB = {}

    # Used job > *
    # Storage for current jobs
    global activeJobDB
    activeJobDB = {}

    # Used jobset > *
    #Storage for current jobsets
    global activeJobsetDB
    activeJobsetDB = {}

    # Used extensively
    # Placeholder for global tick handler
    global tick
    tick = 0

    # Used in main.py
    # Used to terminate game
    global gameExit
    gameExit = False

    # Used extensively
    # placeholder for global player objecgt
    global player
    player = 0

    # Used engine > out.py
    # storage for model output
    global activeOutputDB
    activeOutputDB = []

    # Used engine > event.py
    # storage for model inputs
    global activeInputDB
    activeInputDB = []

    # Used main.py, engine > render.py
    # placeholder for font database
    global fonts
    fonts = 0

    # Used engine > *
    # storage for current events
    global activeEventDB
    activeEventDB = {}

    # Used engine > userinteract > *
    # storage for current models
    global activeModelDB
    activeModelDB = {}

    # Used engine > *
    # storage for current outputs
    global activeOutDB
    activeOutDB = {}

    # Used engine > input.py
    # handles input buffers
    global inputBuffer
    inputBuffer = {}

    # Used extensively
    # entity statistics/configurations
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

    # Used extensively
    # item statistics/configurations
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
        },
        'copperplate': {
            'title': 'Copper Plate',
            'required': {'copper':1},
            'sellPrice': 50,
            'discovered': True,
            'makes': 1,
        },

    }

    # Used settings.py
    # default speed upgrade prices
    default_speed_upgrade = {
        1: 100,
        2: 1000,
        3: 10000,
    }

    # Used settings.py
    # Default speed production modifier
    default_speed_modifier = {
        0: 1,
        1: 2,
        2: 3,
    }

    # Used extensively
    # object settings/configuration
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
                'tickListen': [1],
                'price': 100,
                'discovered': True,
                'speed_upgrades': default_speed_upgrade,
                'speed_upgrades_modifier': default_speed_modifier
            },
        },
        'processor': {
            'factory_press': {
                'title': 'factory_press',
                'tickListen': [1],
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

    # Used main.py
    # Models to be pre-loaded as early as possible
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
        'gamesettings': False,
        'menustartonlinegame': False,
        'menuloading': False,
        'menugameend': False,
        'menujoingame': False,
    }

    # Used main.py
    # Models to be pre-loaded when GAME starts
    global gameExcluseUI
    gameExcluseUI = {
        'menumarketstatus': False,
    }

    # Used webinteract > market.py
    # Holds current cache information
    global marketCache
    marketCache = {}

    # Used webinteract > *
    # Holds current web-game data
    global gameData
    gameData = {'session_id':1, 'game_id':2, 'game_pin':3}

    global authcode
    authcode = None

    global webinteract
    webinteract = {}