# Generated by Django 4.2.4 on 2023-08-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_video_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='publish_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]
