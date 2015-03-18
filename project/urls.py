from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
# from filebrowser.sites import site
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    url(r'^', include('app.urls'), name='main'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/filebrowser/', include(site.urls)),
    # url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^gallery/', include('imagestore.urls', namespace='imagestore')),
)


# urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
)