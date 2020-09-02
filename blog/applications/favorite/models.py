from django.db import models
from django.conf import settings
#app third party
from model_utils.models import TimeStampedModel 
#
from applications.entry.models import Entry
from .managers import FavoritesManager

class Favorites(TimeStampedModel):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user_favorites')
    entry= models.ForeignKey(Entry,on_delete=models.CASCADE, related_name='entry_favorites')

    objects= FavoritesManager()

    class Meta:
        # para que se guarde la entrada de favoritos una sola vez y no que se guarde la misma varias veces
        unique_together=('user','entry')
        verbose_name= 'Favorite entry'
        verbose_name_plural='Favorite entries'

    def __str__(self):
        return self.user

