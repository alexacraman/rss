from django.contrib.sitemaps import Sitemap
from diary.models import BlogPost
from django.urls import reverse


class BlogPostSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return BlogPost.objects.all()
    
    def lastmod(self, obj):
        return obj.publish_date

class StaticSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.7

    def items(self):
        return ['home','contact', 'about', 'gallery']
    
    def location(self, item):
        return reverse(item)