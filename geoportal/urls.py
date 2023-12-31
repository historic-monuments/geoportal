from django.urls import path

from . import views
from .views import MonumentListView, MonumentDetailView, ArticleListView, ArticleDetailView, about

urlpatterns = [
    path("", ArticleListView.as_view(), name="index"),
    path('monuments/', MonumentListView.as_view(), name='monuments_list'),
    path('monuments/<int:pk>/', MonumentDetailView.as_view(), name='monument_detail'),
    path('articles/', ArticleListView.as_view(), name='articles_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('about/', about, name='about')
]
