from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from roof.models import Gallery, Articles, IndexContent, Contact
from tagging.models import Tag
from imagestore.models import Album, Image
from django.contrib.contenttypes.models import ContentType


class IndexPageView(ListView):
    model = Gallery
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['index_content'] = IndexContent.objects.all()
        return context


class ArticlesPageView(ListView):
    template_name = 'articles.html'
    queryset = Articles.objects.filter(is_public=True).order_by('-pub_date')
    paginate_by = 5


class ContactPageView(ListView):
    template_name = 'contact.html'
    model = Contact


class ObjectsPageView(TemplateView):
    template_name = 'objects.html'


class SelArtPageView(DetailView):
    template_name = 'select-article.html'
    model = Articles
    context_object_name = 'art_object'


class SelObjPageView(TemplateView):
    template_name = 'select-objects.html'


class TagSetView(DetailView):
    template_name = 'tag_set.html'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagSetView, self).get_context_data(**kwargs)
        type_a = ContentType.objects.get_for_model(Articles)
        type_i = ContentType.objects.get_for_model(Image)
        context['article_items'] = self.object.items.filter(content_type=type_a)
        f = self.object.items.filter(content_type=type_i)
        context['image_items'] = set(Album.objects.filter(images=f))
        return context