import json
import requests

API_SEARCH = 'https://api.spotify.com/v1/search'
API_ARTIST = 'https://api.spotify.com/v1/artists/'

def search(type, query):
    r = requests.get(API_SEARCH, params={'q': query, 'type': type})
    artists = r.json()[type+'s']['items']

    return artists

def get_artist(artist_id):
    r = requests.get(API_ARTIST + artist_id)
    artist = r.json()

    return artist

def getArtistModel(artist_id):
    json = get_artist(artist_id)
    pass
