from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
     path('stores/', views.stores_index, name="stores_index"),
     path('stores/create/', views.StoreCreate.as_view(), name="stores_create"),
     path('stores/<int:store_id>/', views.store_detail, name="detail"),
     path('stores/<int:store_id>/new_product/', views.new_product, name="new_product"),
     path('stores/<int:store_id>/product_create', views.product_create, name="product_create"),
     path('accounts/signup/', views.signup, name='signup'),
]
