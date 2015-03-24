# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Articles, Gallery, IndexContent, Contact
from django.conf import settings
from mce_filebrowser.admin import MCEFilebrowserAdmin


class ArticlesAdmin(MCEFilebrowserAdmin):
    pass


class IndexContentAdmin(MCEFilebrowserAdmin):
    pass


class ContactAdmin(MCEFilebrowserAdmin):
    pass


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Gallery)
admin.site.register(IndexContent, IndexContentAdmin)
admin.site.register(Contact, ContactAdmin)


