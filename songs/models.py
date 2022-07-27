from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.

class People(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)

    class Meta: 
        ordering = ('name',)

    def __str__(self):
        return self.name

class Artists(models.Model):
    artist_name = models.CharField(max_length=50)
    dob = models.DateField()
    bio = models.TextField()

    class Meta:
        ordering = ('artist_name',)

    def __str__(self):
        return self.artist_name


class Songs(models.Model):
    song_name = models.CharField(max_length = 25)
    release_date = models.DateField()
    artist = models.ManyToManyField('Artists', related_name='songs')
    cover = models.ImageField(upload_to='uploads/', default="uploads/default_music.jpeg")

    class Meta:
        ordering=('song_name',)

    def __str__(self):
        return self.song_name