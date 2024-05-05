from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Monument, Article


# Create your views here.
def about(request):
    return render(request, 'geoportal/about.html')

def mapView(request):
    return render(request, 'geoportal/map.html')


class MonumentListView(ListView):
    model = Monument
    template_name = 'geoportal/monuments_list.html'
    TRANSLATION_MAP = {
        'history': "Історичні об'єкти культурної спадщини",
        'architecture': 'Споруди культового призначення',
        'archeology': "Археологічні об'єкти культурної спадщини",
        'reservation': 'Державні історико-культурні заповідники та музеї',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        monument_type = self.kwargs.get('type')
        translation = self.TRANSLATION_MAP.get(monument_type, "Історичні пам'ятки")
        context['monument_type'] = translation
        return context

    def get_queryset(self):
        monument_type = self.kwargs.get("type")
        if monument_type:
            return Monument.objects.filter(Q(monument_type__icontains=monument_type.lower()))
        else:
            return Monument.objects.all()


class MonumentDetailView(DetailView):
    model = Monument
    template_name = 'geoportal/monument_detail.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'geoportal/articles_list.html'
    ordering = ['-created_date']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'geoportal/article_detail.html'

class SearchResultsView(ListView):
    model = Monument
    template_name = "geoportal/search_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Monument.objects.filter(Q(name__icontains=query.lower()) | Q(name__icontains=query.capitalize()))
        else:
            return Monument.objects.all()
