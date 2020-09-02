from datetime import timedelta, datetime
#
from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy
# models import 
from applications.entry.models import Entry

class EntrySitemap(Sitemap):
    change_freq= 'weekly'
    priority= 0.8
    protocol='https'

    def items(self):
        return Entry.objects.filter(public=True)

    #chronological order urls   
    def lastmod(self,obj):
        return obj.created

class Sitemap(Sitemap):
    protocol='https'

    def __init__(self, names):
        self.names= names

    def items(self):
        return self.names   

    def change_freq(self, obj):
        return 'weekly'         

    def lastmod(self,obj):
        return datetime.now()

    def location(self,obj):
        return reverse_lazy(obj)