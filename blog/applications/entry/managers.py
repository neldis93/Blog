from django.db import models


class EntryManager(models.Manager):

    def entry_cover_page(self):
        return self.filter(
            public=True,
            cover_page=True,    
        ).order_by('-created').first()

    def entry_home(self):
        # devuelve las ultimas 4 entradas en home
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]

    def entry_recent(self):
        # devuelve las ultimas 6 entradas recientes
        return self.filter(
            public=True,
        ).order_by('-created')[:6]

    def search_entry(self, kword, category):
        # procedimiento para buscar entradas por categoria o palabras claves
        if len(category) > 0:
            return self.filter(
                category__short_name= category,
                title__icontains=kword,
                public=True,
            ).order_by('-created')

        else:
            return self.filter(
                title__icontains=kword,
                public=True,
            ).order_by('-created')
            
