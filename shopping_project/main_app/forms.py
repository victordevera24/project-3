from django.forms import ModelForm
from .models import Product, Review

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'sale_price', 'sale_end']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'review', 'rating']