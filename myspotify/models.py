from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artist(models.Model):
    user = models.ManyToManyField(User, related_name='artists')
    href = models.CharField(max_length=300)
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, default='artist')
    uri = models.CharField(max_length=200)
    image = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name

class Album(models.Model):
    user = models.ManyToManyField(User, related_name='albums')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_type = models.CharField(max_length=50)
    href = models.CharField(max_length=300)
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, default='album')
    uri = models.CharField(max_length=200)
    image = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name

class Track(models.Model):
    user = models.ManyToManyField(User, related_name='tracks')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    disc_number = models.IntegerField()
    duration_ms = models.IntegerField()
    explicit = models.BooleanField()
    href = models.CharField(max_length=300)
    id = models.CharField(max_length=100, primary_key=True)
    is_playable = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    preview_url = models.CharField(max_length=200)
    type = models.CharField(max_length=20, default='track')
    uri = models.CharField(max_length=200)
    image = models.CharField(max_length=300, default='')
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name
