import facebook
import requests
import ConfigParser


config = ConfigParser.ConfigParser()
config.read('config/client.cfg')

access_token=config.get('fb','access_token')
fb_api_version=config.get('fb','fb_api_version')

graph = facebook.GraphAPI(
        access_token=access_token,
        version=fb_api_version)

places = graph.search(
        type='page',
        q='Indian Grocery Florida',
        center='0,0',
        distance=5000,
        fields='name, emails, location, about')

#print places['paging']['next']

for place in places['data']:
    try:
        if place['emails'] and place['location']['country'] == 'United States':
            print '{}, {}, {}'.format( ','.join(place['emails']), place['name'], place['location']['city'])
    except:
        pass

places1 = requests.get(places['paging']['next']).json()
for place in places1['data']:
    try:
        if place['emails'] and place['location']['country'] == 'United States':
            print '{}, {}, {}'.format( ','.join(place['emails']), place['name'], place['location']['city'])
    except:
        pass
places2 = requests.get(places1['paging']['next']).json()
for place in places2['data']:
    try:
        if place['emails'] and place['location']['country'] == 'United States':
            print '{}, {}, {}'.format( ','.join(place['emails']), place['name'], place['location']['city'])
    except:
        pass

places3 = requests.get(places2['paging']['next']).json()
for place in places3['data']:
    try:
        if place['emails'] and place['location']['country'] == 'United States':
            print '{}, {}, {}'.format( ','.join(place['emails']), place['name'], place['location']['city'])
    except:
        pass

places4 = requests.get(places3['paging']['next']).json()
for place in places4['data']:
    try:
        if place['emails'] and place['location']['country'] == 'United States':
            print place['emails'].decode()
    except:
        pass

places5 = requests.get(places4['paging']['next']).json()
for place in places5['data']:
    try:
        if place['emails'] and place['location']['country'] == 'United States':
            print place['emails'].decode()
    except:
        pass
