from django.contrib.sitemaps import Sitemap
from .models import Blog
 
 
class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.created_at
        
    def location(self,obj):
        return '/post/%s' % (obj.link)