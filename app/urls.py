from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from .views import IndexPageView, ArticlesPageView, ContactPageView, ObjectsPageView, SelArtPageView, SelObjPageView,\
    TagSetView


urlpatterns = patterns('',
       url(r'^$', IndexPageView.as_view(), name='index'),
       url(r'^articles/$', ArticlesPageView.as_view(), name='articles'),
       url(r'^contact/$', ContactPageView.as_view(), name='contact'),
       url(r'^objects$', ObjectsPageView.as_view(), name='objects'),
       url(r'^sel-art/(?P<pk>\d+)$', SelArtPageView.as_view(), name='sel_atr'),
       url(r'^tag_set/(?P<pk>\d+)$', TagSetView.as_view(), name='tag_set'),
       url(r'^sel-obj/$', SelObjPageView.as_view(), name='sel_obj'),

)

