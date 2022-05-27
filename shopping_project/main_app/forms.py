from django.forms import ModelForm
from django.views.generic.edit import CreateView
from .models import Product, Review, WishList

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'sale_price', 'sale_end']


class WishListForm(ModelForm):
    class Meta:
        model = WishList
        fields = ['name']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'review', 'rating']

