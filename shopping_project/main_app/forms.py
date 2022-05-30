from django.forms import ModelForm
from .models import Product, Review, WishList


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'on_sale', 'sale_price', 'sale_end']


class WishListForm(ModelForm):
    class Meta:
        model = WishList
        fields = ['name']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'review', 'rating']

    def clean(self):

        super(ReviewForm, self).clean()

        rating = self.cleaned_data.get('rating')

        if rating > 5:
            self.errors['rating'] = self.error_class([
                'Rating must be 1-5'
            ])

        return self.cleaned_data