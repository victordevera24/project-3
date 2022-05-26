from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
     path('stores/', views.stores_index, name="stores_index"),
     path('stores/create/', views.StoreCreate.as_view(), name="stores_create"),
     path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
     path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='stores_delete'),
     path('stores/<int:store_id>/', views.store_detail, name="detail"),
     path('stores/<int:store_id>/new_product/', views.new_product, name="new_product"),
     path('stores/<int:store_id>/product_create', views.product_create, name="product_create"),
     path('accounts/signup/', views.signup, name='signup'),
     path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='products_update'),
     path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='products_delete'),
     path('product/<int:product_id>/', views.product_detail, name='product_detail'),
     path('product/<int:product_id>/new_wishlist', views.new_wishlist, name='new_wishlist'),
     path('products/<int:product_id>/wishlist_create/', views.wishlist_create, name='wishlist_create'),
]

