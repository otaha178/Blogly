from django.contrib.sitemaps.views import sitemap
from django.urls import path

from blog.feed import LatestPostsFeed
from blog.sitemaps import PostSitemap
from . import views

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('post/new', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
