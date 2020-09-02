from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
# solo para usuarios logeados
from django.contrib.auth.mixins import LoginRequiredMixin 

from django.views.generic import View, ListView, DeleteView

from .models import Favorites
from applications.entry.models import Entry

class UserPageListView(LoginRequiredMixin,ListView):
    template_name = "favorite/profile.html"
    context_object_name= 'entry_user'
    login_url= reverse_lazy('users_app:user_login')

    def get_queryset(self):
        
        return Favorites.objects.entry_user(self.request.user) # esto trae el usuario activo de la sesion


class AddFavoriteView( LoginRequiredMixin, View):
    login_url= reverse_lazy('users_app:user_login')

    def post(self,request, *args, **kwargs):
        # recuperar un usuario
        userr= self.request.user
        entries= Entry.objects.get(id=self.kwargs['pk'])
        # registramos favorito
        Favorites.objects.create(
            user=userr,
            entry= entries,
        )
        return HttpResponseRedirect(
            reverse('favorite_app:profile',)
        )


class FavoriteDeleteView(DeleteView):
    model = Favorites
    success_url= reverse_lazy('favorite_app:profile')
