from django.conf.urls import patterns, url
from .views import IndexPageView, ArticlesPageView, ContactPageView, SelArtPageView, TagSetView


urlpatterns = patterns('',
       url(r'^$', IndexPageView.as_view(), name='index'),
       url(r'^articles/$', ArticlesPageView.as_view(), name='articles'),
       url(r'^contact/$', ContactPageView.as_view(), name='contact'),
       url(r'^article/(?P<slug>[\w-]+)$', SelArtPageView.as_view(), name='sel_atr'),
       url(r'^tag_set/(?P<pk>\d+)$', TagSetView.as_view(), name='tag_set'),

)

