from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
# Seo
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import EntrySitemap, Sitemap

urlpatterns_main = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.entry.urls')),
    re_path('', include('applications.favorite.urls')),
    # url for ckeditor
    re_path(r'^ckeditor/',include('ckeditor_uploader.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# site map object that generates xml
sitemaps={
    # url root
    'site':Sitemap(
        ['home_app:index']
    ),
    'entries': EntrySitemap

}

urlpatterns_sitemap=[
    path('sitemap.xml', sitemap,{'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

# we concatenate the urlpatterns because it is the one who reads the urls.py
urlpatterns = urlpatterns_main + urlpatterns_sitemap