from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Artist

# Create your views here.
def index(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists
    }
    return render(request, 'myspotify/artists/index.html', context)

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'myspotify/artists/detail.html', {'artist': artist})
