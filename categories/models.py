from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from tags.models import TaggedItem

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    tags = GenericRelation(TaggedItem, related_query_name='category')
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Cagegories'

    def __str__(self):
        return self.title
