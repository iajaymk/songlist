# Generated by Django 4.0.6 on 2022-07-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_alter_artists_artist_name_alter_people_name_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='artist',
        ),
        migrations.AddField(
            model_name='songs',
            name='artist',
            field=models.ManyToManyField(related_name='songs', to='songs.artists'),
        ),
    ]
