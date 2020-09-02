from django.db import models

class FavoritesManager(models.Manager):

    def entry_user(self, userss): # userss es una variable nueva que creo para pasarsela al user del models.py
        return self.filter(
            # entry viene del parametro que se hizo en el models.py
            entry__public=True,
            user=userss
        ).order_by('-created')