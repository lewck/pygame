import settings
settings.init()
from engine.userinteract.model.factoryminermenu import factoryminermenu

modelID = 51
uid = 'factoryminermenu'

model = eval(uid + '(id = modelID)')

print(model)