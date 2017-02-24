from django.conf.urls import url

from . import views

app_name = 'myspotify'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^artists/(?P<artist_id>[\w]+)$', views.artist_detail, name='artist_detail'),
    url(r'^artists/load/(?P<artist_id>[\w]+)$', views.artists_load, name='artists_load'),
    url(r'^artists/save/(?P<artist_id>[\w]+)$', views.artists_save, name='artists_save'),
]
