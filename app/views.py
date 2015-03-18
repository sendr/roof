from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Gallery, Articles, IndexContent


class IndexPageView(ListView):
    model = Gallery
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['index_content'] = IndexContent.objects.all()
        return context


class ArticlesPageView(ListView):
    template_name = 'articles.html'
    queryset = Articles.objects.filter(is_public=True)
    paginate_by = 5


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class ObjectsPageView(TemplateView):
    template_name = 'objects.html'


class SelArtPageView(DetailView):
    template_name = 'select-article.html'
    model = Articles
    context_object_name = 'art_object'

    # def get_context_data(self, **kwargs):
    #     context = super(SelArtPageView, self).get_context_data(**kwargs)
    #     context['tags'] = Tag.objects.get(id=2)
    #     print dir(context['tags'])
    #     return context


class SelObjPageView(TemplateView):
    template_name = 'select-objects.html'