import urllib.request
import urllib.parse
import json
import csv

# Below is the script used to call the api during the demand testing stages
# This script is standalone from the main code
# This script assumes variables that are only set in the development environment (local SQL) so
# it should not be run remotely, or distributed with the project.

token = 'ngyBtvxbC2dPQg2f8lmZMVAceGQo2q0s'


def getDemand():
    # Get response
    data = urllib.request.urlopen(
        'http://localhost/pygame/kernel.php?authorisation_token=ngyBtvxbC2dPQg2f8lmZMVAceGQo2q0s&function=getmarketdemand&session_id=487&sortby=487')
    # Decode response
    decodedData = data.read().decode('utf-8')
    # Encode to JSON response
    jsonData = json.loads(decodedData)

    for each in jsonData:
        if (each['itemid'] == 'metalbrass'):
            return each['current_demand_addition']


def reduceDemand():
    # Get response
    data = urllib.request.urlopen(
        'http://localhost/pygame/kernel.php?authorisation_token=ngyBtvxbC2dPQg2f8lmZMVAceGQo2q0s&function=reduceMarketDemand&game_id=1&item_id=metalbrass&quantity=1')
    # Decode response
    decodedData = data.read().decode('utf-8')
    # Encode to JSON response
    jsonData = json.loads(decodedData)


results = []

for i in range(0, 1000):
    results.append([i, getDemand()])
    reduceDemand()

with open('results.csv', 'w') as csvfile:
    fieldnames = ['call', 'modifier']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    for each in results:
        writer.writerow({'call': each[0], 'modifier': each[1]})

