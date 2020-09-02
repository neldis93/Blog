from django.db import models
#app third party
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    title = models.CharField('Name', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Title of us', max_length=50)
    about_text = models.TextField()
    contact_email = models.EmailField('Contact email', blank=True, null=True)
    phone_number= models.CharField('Contact phone',max_length=20)

    class Meta:
        verbose_name= 'Homepage'
        verbose_name_plural='Homepage'

    def __str__(self):
        return self.title


class Suscribers(TimeStampedModel):
    email= models.EmailField('Name', max_length=60)

    class Meta:
        verbose_name='Suscriber'
        verbose_name_plural='Suscribers'

    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    first_name = models.CharField('First name', max_length=40)
    last_name= models.CharField('Last name', max_length= 40)
    email= models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'

    def __str__(self):
        return self.first_name + ' ' + self.last_name