
from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


class PublishStateOptions(models.TextChoices):
    # CONSTANT = DB_VALUE, USER_DISPLAY_VALUE
    PUSLISH = 'PU', 'Publish'
    DRAFT = 'DR', 'Draft'
    # UNLISTED = 'UN', 'Unlisted'
    # PRIVATE = 'PR', 'Private'


class VideoQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            state=PublishStateOptions.PUSLISH,
            publish_timestamp__lte=timezone.now()
        )


class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(
        max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True, null=True)

    objects = VideoManager()

    @property
    def is_published(self):
        return self.active

    # def save(self, *args, **kwargs):
        # if self.state == self.VideoStateOptions.PUSLISH and self.publish_timestamp is None:
        #     self.publish_timestamp = timezone.now()
        # elif self.state == self.VideoStateOptions.DRAFT:
        #     self.publish_timestamp = None
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        # super().save(*args, **kwargs)


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


def publish_state_pre_save(sender, instance, *args, **kwargs):
    is_publish = instance.state == PublishStateOptions.PUSLISH
    is_draft = instance.state == PublishStateOptions.DRAFT
    if is_publish and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
    elif is_draft:
        instance.publish_timestamp = None


pre_save.connect(publish_state_pre_save, sender=Video)


def slugify_pre_save(sender, instance, *args, **kwargs):
    title = instance.title
    slug = instance.slug
    if slug is None:
        instance.slug = slugify(title)


pre_save.connect(slugify_pre_save, sender=Video)
