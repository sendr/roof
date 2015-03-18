# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Articles, Gallery, IndexContent
from django.conf import settings
from mce_filebrowser.admin import MCEFilebrowserAdmin


# @admin.register(Entry,Projects)
# class RegAdmin(admin.ModelAdmin):pass


class ArticlesAdmin(MCEFilebrowserAdmin):
    pass
    # fieldsets = ((None, {'fields': ['name', 'image', 'order', 'tags']}),)



admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Gallery)
admin.site.register(IndexContent)

