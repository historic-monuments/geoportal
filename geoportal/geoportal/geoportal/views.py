from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Monument, Article


# Create your views here.
def about(request):
    return render(request, 'geoportal/about.html')

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
