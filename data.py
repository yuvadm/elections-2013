import csv
import json
import requests

from pprint import pprint

def fetch_geocodes(cities):
    d = {}
    url = 'http://maps.googleapis.com/maps/api/geocode/json'
    for city in cities:
        print 'fetching ' + city
        res = requests.get(url, params={
            'address': city,
            'sensor': 'false'
        })
        city = unicode(city.decode('utf8')).encode('utf8')
        d[city] = json.loads(res.content, encoding='utf8')
    return d

with open('data.csv', 'r') as f:
    c = csv.reader(f, delimiter=',', quotechar='"')
    data = [x for x in c]
    parties = data[0][1:]
    cities = map(lambda x: x[0], data)
    city_data = fetch_geocodes(cities)
    print city_data
    with open('data.json', 'w') as out:
        json.dump(city_data, out, indent=4, ensure_ascii=False)
