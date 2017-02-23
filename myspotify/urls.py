from django.conf.urls import url

from . import views

app_name = 'myspotify'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^artists/(?P<artist_id>[\w]+)/$', views.detail, name='detail')
]
