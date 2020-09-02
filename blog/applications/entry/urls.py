from django.urls import path
from . import views


app_name = "entry_app"

urlpatterns = [
    path('inputs/', views.EntryListView.as_view(), name='entry'), 
    path('detail-inputs/<slug>/', views.EntryDetailView.as_view(), name='detail_inputs')
]