# coding: utf-8

from django.db import models


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.slug


## Filtreerib välja, mis on avaldatud
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    objects = EntryQuerySet.as_manager() 

    def entry(self):
        return self.title

    ## Järjekord ja mitmus.?
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created_at"]