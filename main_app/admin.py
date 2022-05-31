from django.contrib import admin

from .models import Store, Product, Review, WishList


# Register your models here.
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(WishList)
