from django.urls import path
from . import views


app_name = "favorite_app"

urlpatterns = [
    path('profile/', views.UserPageListView.as_view(), name='profile'),
    # le pasamos un pk porque estamos recuperandolo en el entry= Entry.objects.get(id=self.kwargs['pk'])
    path('Add-entry/<pk>/',views.AddFavoriteView.as_view(), name='favorite_add'),
    path('delete-favorite/<pk>/', views.FavoriteDeleteView.as_view(), name='favorite_delete'),   
]

    