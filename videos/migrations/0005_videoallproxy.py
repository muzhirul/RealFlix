# Generated by Django 4.2.4 on 2023-08-24 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_video_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoAllProxy',
            fields=[
            ],
            options={
                'verbose_name': 'All Videos',
                'verbose_name_plural': 'All Videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
    ]
