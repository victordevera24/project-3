from django.forms import ModelForm
from .models import Product, WishList
from django.views.generic.edit import CreateView

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'sale_price', 'sale_end']

class WishListForm(ModelForm):
    class Meta:
        model = WishList
        fields = ['name']