from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Artist
from .spotifyapi import parser as api
import requests, json

# Create your views here.
def index(request):
    return render(request, 'myspotify/index.html')

@login_required()
def search(request):
    if (request.method == 'POST'):
        type = request.POST.get('type')
        query = request.POST.get('query')

        results = api.search(type, query)

        context = {
            'results': results
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

    return render(request, 'myspotify/artists/index.html', context)
