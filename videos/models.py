from re import M
from tabnanny import verbose
from weakref import proxy
from django.db import models

# Create your models here.


class Video(models.Model):
    class VideoStateOptions(models.TextChoices):
        # CONSTANT = DB_VALUE, USER_DISPLAY_VALUE
        PUSLISH = 'PU', 'Publish'
        DRAFT = 'DR', 'Draft'
        # UNLISTED = 'UN', 'Unlisted'
        # PRIVATE = 'PR', 'Private'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    state = models.CharField(
        max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT)

    @property
    def is_published(self):
        return self.active


class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'All Videos'
        verbose_name_plural = 'All Videos'


class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Published Videos'
        verbose_name_plural = 'Published Videos'
