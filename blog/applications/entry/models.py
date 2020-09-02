from datetime import timedelta, datetime
#
from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
#app third party
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
#managers
from .managers import EntryManager


class Category(TimeStampedModel):
    short_name = models.CharField('Short name', max_length=15)
    name = models.CharField('Name', max_length=30)


    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    """etiquetas de un articulo"""

    name = models.CharField('Name', max_length=30)

    class Meta:
        verbose_name='Label'
        verbose_name_plural='Tags'

    def __str__(self):
        return self.name

class Entry(TimeStampedModel):
    """modelo para entradas o articulo"""

    # con el AUTH_USER_MODEL hago referencia a nuestra clase User del models.py de la applications user 
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag)
    title = models.CharField('title',max_length=200)
    summary = models.TextField('Summary')
    content= RichTextUploadingField('Content')
    public = models.BooleanField(default=False)
    image = models.ImageField('Image', upload_to='Entry')
    cover_page = models.BooleanField(default=False)
    in_home= models.BooleanField(default=False)

    slug = models.SlugField(editable=False, max_length=300)

    objects= EntryManager()

    class Meta:
        verbose_name= 'Entry'
        verbose_name_plural= 'Inputs'

    def __str__(self):
        return self.title

    # Seo generate xml
    def get_absolute_url(self):
        return reverse_lazy(
            'entry_app:detail_inputs',
            kwargs={'slug':self.slug}
        )

    #generar el slug
    def save(self, *args, **kwargs):
        # calculamos el total de segundos de la hora actual
        now= datetime.now()
        total_time= timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds= now.second
        )
        seconds= int(total_time.total_seconds())
        slug_unique= '%s %s' % (self.title, str(seconds))

        self.slug= slugify(slug_unique)
        super(Entry,self).save(*args, **kwargs)