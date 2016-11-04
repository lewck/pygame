import urllib.request
import urllib.parse
import json

import settings

class base:
    def __init__(self):
        #Authenticate with server
        self.auth()

    def requestCall(self, function, params = 0):
        data = {}

        data['function'] = function

        if(params != 0):
            for key, value in params.items():
                data[key] = value

        data['authorisation_token'] = self.authCode

        print(data)

        url_values = urllib.parse.urlencode(data)
        print(url_values)
        url = 'http://localhost/pygame/kernal.php'
        full_url = url + '?' + url_values
        data = urllib.request.urlopen(full_url)
        decodedData = data.read().decode('utf-8')

        jsonData = json.loads(decodedData)

        if('fail' in jsonData):
            print('Webinteract fail '+str(jsonData['fail']))
            return False

        return jsonData


    def auth(self):
        self.authCode = 0
        self.authCode = self.requestCall('auth', { 'apikey': settings.APIKEY })['authorisation_token']

        if(self.authCode):
            return True
        return False