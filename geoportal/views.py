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
