from re import S
from django.contrib import admin
from .models import People, Artists, Songs


@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ['song_name','cover', 'release_date']


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):
    list_display = ['artist_name','dob','bio']