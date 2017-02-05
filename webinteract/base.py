import urllib.request
import urllib.parse
import json

import settings

class base:
    def __init__(self):
        # Authenticate with server
        self.auth()

    def requestCall(self, function, params = 0):
        data = {}
        data['function'] = function

        # Assign parameters to local var if provided
        if(params != 0):
            for key, value in params.items():
                data[key] = value

        data['authorisation_token'] = settings.authcode


        # Encode GET params using urllib
        url_values = urllib.parse.urlencode(data)



        url = 'http://'+settings.remoteURL+'/pygame/kernel.php'

        # Collate url with get vars
        full_url = url + '?' + url_values

        # Print for debugging
        print('------------------')
        print('Calling Webserver')
        print(data)
        print(url_values)
        print('------------------')

        # Attempt web call
        try:
            # Get response
            data = urllib.request.urlopen(full_url)
            # Decode response
            decodedData = data.read().decode('utf-8')
            # Encode to JSON response
            jsonData = json.loads(decodedData)

        except urllib.error.URLError:
            # Fail (server down?), create json response anyway
            print('Error Connecting')
            jsonData = {}
            jsonData['fail'] = '404'
            print('Webinteract fail')

        return jsonData


    def auth(self):
        # Authenticate with the webserver if authcode not provided
        if(settings.authcode == None):
            # Request auth call with global api key, save to global or fail
            authcode = self.requestCall('auth', { 'apikey': settings.APIKEY })

            if(authcode):
                settings.authcode = authcode['authorisation_token']
                return True

            return False