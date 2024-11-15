from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap
from django.urls import path
from . import views



sitemaps = {
    'blog':BlogSitemap
}


urlpatterns = [
    path('', views.home,name = 'home'),
    path('about/', views.about,name = 'about'),
    path('services/', views.services,name = 'services'),
    path('blog/', views.blog,name = 'blog'),
    path('team/', views.team,name = 'team'),
    path('contact/', views.contact,name = 'contact'),
    path('contact_form/', views.contact_form,name = 'contact_form'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    
]
