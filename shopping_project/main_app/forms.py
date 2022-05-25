from django.forms import ModelForm
from .models import Product
from django.views.generic.edit import CreateView

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'sale_price', 'sale_end']