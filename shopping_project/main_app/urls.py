from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
     path('stores/', views.stores_index, name="stores_index"),
     path('stores/create/', views.StoreCreate.as_view(), name="stores_create"),
]
