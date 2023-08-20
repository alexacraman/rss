"""rss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin 
from django.urls import path, include
from django.conf.urls.static import static
from search.views import search_view
from .views import (home, about, contactView, gallery, SignUpView, privacy_policy,terms_conditions, robots_txt)

from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogPostSitemap, StaticSitemap

sitemaps = {
    'static': StaticSitemap,
    'blog':BlogPostSitemap,
}
urlpatterns = [
    path('', home, name='home'),
    path('diary/', include('diary.urls')),
    path('process/', include('process.urls', namespace='process')),
    path('contact/', contactView, name='contact'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('search/', search_view),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt),
    path('policy/', privacy_policy, name='policy'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)