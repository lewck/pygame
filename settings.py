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

    global processingDB
    processingDB = {
        'press':{
            'transformations': {
                'metalcopper': {
                    'required': 2,
                    'produces': {'copperplate': 2}
                },
                'metalzinc': {
                    'required': 2,
                    'produces': {'zincplate': 2}
                },
                'metaltin': {
                    'required': 2,
                    'produces': {'tinplate': 2}
                },
                'metalbronze': {
                    'required': 2,
                    'produces': {'bronzeplate': 2}
                },
                'metalbrass': {
                    'required': 2,
                    'produces': {'brassplate': 2}
                },
            }
        },
        'puncher': {
            'transformations': {
                'copperplate': {
                    'required': 1,
                    'produces': {'copperdisk': 5}
                }
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
            'mineable': True,
        },
        'metalzinc': {
            'title': 'Zinc',
            'required': {},
            'sellPrice': 5,
            'discovered': True,
            'makes': 1,
            'mineable': True,
        },
        'metaltin': {
            'title': 'Tin',
            'required': {},
            'sellPrice': 5,
            'discovered': True,
            'makes': 1,
            'mineable': True,
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
        'copperplate': {
            'title': 'Copper Plate',
            'sellPrice': 50,
            'discovered': True
        },
        'zincplate': {
            'title': 'Zink Plate',
            'sellPrice': 50,
            'discovered': True
        },
        'tinplate': {
            'title': 'Tin Plate',
            'sellPrice': 50,
            'discovered': True
        },
        'bronzeplate': {
            'title': 'Bronze Plate',
            'sellPrice': 50,
            'discovered': True
        },
        'brassplate': {
            'title': 'Copper Plate',
            'sellPrice': 50,
            'discovered': True
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
        'copperdisk': {
            'title': 'Copper Disk',
            'sellPrice': 100,
            'discovered': True
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
                'price': 0,
                'discovered': False,
            }
        },
        'storage': {

        },
        'storageVehicles': {
            'garage': {
                'title': 'garage',
                'tickListen': [],
                'discovered': True,
                'price': 100,
            },
        },
        'producer': {
            'factory_parts': {
                'title': 'factory_parts',
                'tickListen': [2],
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
            'factory_puncher': {
                'title': 'factory_puncher',
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
                'price': 5,
                'discovered': True,
            },
        },
        'exports': {
            'exports': {
                'title': 'exports',
                'tickListen': [5],
                'price': 50,
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