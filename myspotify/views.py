from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Artist, Album
from .spotifyapi import api
import requests, json

# Create your views here.
def index(request):
    return render(request, 'myspotify/index.html')

@login_required()
def search(request):
    if (request.method == 'POST'):
        type = 'artist'
        query = request.POST.get('query')

        results = api.search(type, query)

        context = {
            'results': results,
            'query': query
        }

        return render(request, 'myspotify/search/index.html', context)

    return render(request, 'myspotify/search/index.html')

@login_required()
def artists(request):
    artists = request.user.artists.all()
    context = {
        'artists': artists
    }
    return render(request, 'myspotify/artists/index.html', context)

@login_required()
def artists_save(request, artist_id):

    json = api.get_artist(artist_id)

    artist = Artist()

    artist.name = json['name']
    artist.href = json['href']
    artist.id = json['id']
    artist.type = json['type']
    artist.uri = json['uri']
    artist.image = json['images'][0]['url'] if json['images'] else ''

    artist.save()

    user = request.user
    user.artists.add(artist)

    print(user.artists.all())

    user.save()
    print(user.artists.all())

    artists = Artist.objects.all()
    context = {
        'artists': artists
    }

    return redirect('myspotify:artists')

@login_required()
def artists_load(request, artist_id):

    json = api.get_artist_albums(artist_id)
    user = request.user
    artist = user.artists.get(id=artist_id)

    for album in json['items']:

        if artist.album_set.filter(name=album['name']).first():
            print(album['name'])
            continue

        new_album = Album()

        new_album.artist = artist
        new_album.id = album['id']
        new_album.name = album['name']
        new_album.href = album['href']
        new_album.album_type = album['album_type']
        new_album.uri = album['uri']
        new_album.image = album['images'][0]['url'] if album['images'] else ''

        new_album.save()
        artist.album_set.add(new_album)

    artist.new = False

    artist.save()

    return redirect('myspotify:artist_detail', artist_id=artist_id)

@login_required()
def artist_detail(request, artist_id):

    artist = request.user.artists.get(id=artist_id)

    context = {
        'artist': artist
    }

    return render(request, 'myspotify/artists/details.html', context)
