from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from roof.models import Address


urlpatterns = patterns('',
    url(r'^', include('roof.urls'), name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^gallery/', include('imagestore.urls', namespace='imagestore'), {
        "addresses": Address.objects.all(),
    }),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
)