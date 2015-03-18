# -*- coding: utf-8 -*-
from django.db import models
# from imagestore.models.image import Image
from tinymce.models import HTMLField
from django.utils import timezone
import tagging
from taggit.managers import TaggableManager
from tagging.fields import TagField



# class Entry(models.Model):
#     name = models.CharField(max_length=100)
#     date = models.DateTimeField()
#     image = models.ImageField()
#     entry_body = models.TextField()
#     related_entries = models.ForeignKey('self')
#
# class Projects(models.Model):
#     from imagestore.models.album import Album
#
#     name =  models.CharField(max_length=100)
#     descr = models.TextField()
#     gallery = models.ForeignKey(Album)

#
# class TagModel(models.Model):
#     name = models.CharField(max_length=30, blank=True, null=True)
#
#     def __unicode__(self):
#         return self.name


# class AlbumTag(Album):
#     tag = models.ForeignKey(TagModel, blank=True, null=True)
#
#     def __unicode__(self):
#         return self.tag


class Articles(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    pub_date = models.DateTimeField(default=timezone.now())
    content = HTMLField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    is_public = models.BooleanField('Is public', default=True)
    tags = TagField(blank=True)

    class Meta():
        verbose_name = u"Статьи"
        verbose_name_plural = u"Статьи"

    def __unicode__(self):
        return self.name


# tagging.register(Articles)

class Gallery(models.Model):
    tittle = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='gallery')

    def __unicode__(self):
        return self.tittle


class IndexContent(models.Model):
    tittle = models.CharField(max_length=30)
    content = HTMLField(blank=True, null=True)

    def __unicode__(self):
        return self.tittle