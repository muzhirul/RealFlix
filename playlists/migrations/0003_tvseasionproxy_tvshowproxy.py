# Generated by Django 4.2.4 on 2023-08-26 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0002_playlist_order_playlist_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVSeasionProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('playlists.playlist',),
        ),
        migrations.CreateModel(
            name='TVShowProxy',
            fields=[
            ],
            options={
                'verbose_name': 'TV Show',
                'verbose_name_plural': 'TV Shows',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('playlists.playlist',),
        ),
    ]
