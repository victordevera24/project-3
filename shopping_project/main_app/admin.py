from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Store, Product, Photo, Review, User


# Register your models here.
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Review)
admin.site.register(User, UserAdmin)
