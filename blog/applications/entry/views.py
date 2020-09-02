from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Entry, Category

#blog
class EntryListView(ListView):
    template_name = "entry/list.html"
    context_object_name= 'entry'
    paginate_by= 3  

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        return context
    
    def get_queryset(self):
        kword= self.request.GET.get('kword','')
        category= self.request.GET.get('category','')
        # consulta  de busqueda
        result= Entry.objects.search_entry(kword, category)
        return result

#click al link y mostrar el contenido
class EntryDetailView(DetailView):
    template_name = "entry/detail.html"
    model = Entry
    context_object_name= 'entry_detail'