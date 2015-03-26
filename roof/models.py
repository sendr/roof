# -*- coding: utf-8 -*-
from django.db import models
# from imagestore.models.image import Image
from tinymce.models import HTMLField
from django.utils import timezone
import tagging
from taggit.managers import TaggableManager
from tagging.fields import TagField


class Articles(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    pub_date = models.DateTimeField(default=timezone.now())
    content = HTMLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    is_public = models.BooleanField('Is public', default=True)
    tags = TagField(blank=True)

    class Meta():
        verbose_name = u"Статьи"
        verbose_name_plural = u"Статьи"

    def __unicode__(self):
        return self.name

    @property
    def is_article(self):
        return True


# tagging.register(Articles)

class Gallery(models.Model):
    tittle = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='gallery')

    class Meta():
        verbose_name = u"Фотогалерея"
        verbose_name_plural = u"Фотогалерея"

    def __unicode__(self):
        return self.tittle


class IndexContent(models.Model):
    tittle = models.CharField(max_length=30)
    content = HTMLField(blank=True, null=True)

    class Meta():
        verbose_name = u"О нас"
        verbose_name_plural = u"О нас"

    def __unicode__(self):
        return self.tittle


class Contact(models.Model):
    tittle = models.CharField(max_length=50)
    content = HTMLField(blank=True, null=True)

    class Meta():
        verbose_name = u'Контакты'
        verbose_name_plural = u'Контакты'

    def __unicode__(self):
        return self.tittle


class Phone(models.Model):
    name = models.CharField(max_length=30)

    class Meta():
        verbose_name = u'Телефон'
        verbose_name_plural = u'Телефоны'

    def __unicode__(self):
        return self.name


class Email(models.Model):
    name = models.EmailField(max_length=30)

    class Meta():
        verbose_name = u'Электронная почта'
        verbose_name_plural = u'Электронная почта'

    def __unicode__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=50)

    class Meta():
        verbose_name = u'Адрес'
        verbose_name_plural = u'Адреса'

    def __unicode__(self):
        return self.name