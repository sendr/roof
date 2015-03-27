from django.views.generic import ListView, DetailView
from roof.models import Gallery, Articles, IndexContent, Contact, Address, Email, Phone
from tagging.models import Tag
from imagestore.models import Album, Image
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class Footer(object):
    addresses = Address.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()


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


class SelArtPageView(DetailView):
    template_name = 'select-article.html'
    model = Articles
    context_object_name = 'art_object'


class TagSetView(DetailView):
    template_name = 'tag_set.html'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagSetView, self).get_context_data(**kwargs)
        type_a = ContentType.objects.get_for_model(Articles)
        type_i = ContentType.objects.get_for_model(Image)
        article_items = list(self.object.items.filter(content_type=type_a))
        f = self.object.items.filter(content_type=type_i)
        image_items = list(set(Album.objects.filter(images=f.values_list('object_id', flat=True))))
        paginator = Paginator(article_items + image_items, 5)
        page = self.request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context['items'] = items
        context['paginator'] = paginator
        return context