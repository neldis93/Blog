import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, CreateView

from applications.entry.models import Entry
from .models import Home
from .forms import SuscriberForm, ContactForm

#class TestPlantilla(TemplateView):
 #   template_name = "plantillas/register.html"


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # cargamos home
        # latest recupera el ultimo registro en base a un parametro que le demos, 
        # es este caso le estamos diciendo que lo triaga por la ultima en base a la fecha de creacion('created')
        context['home']= Home.objects.latest('created')
        # contexto de portada
        context['cover_page']= Entry.objects.entry_cover_page()
        # contexto para los articulos en home
        context['entry_home']= Entry.objects.entry_home()
        # entradas recientes
        context['entry_recent']= Entry.objects.entry_recent()
        # Enviamos formulario de suscripcion 
        context['form']= SuscriberForm

        return context
    


class SuscriberCreateView(CreateView):
    form_class= SuscriberForm
    success_url= '.' # se refresque en la misma pagina


class ContactCreateView(CreateView):
    form_class= ContactForm
    success_url= '.'
    
