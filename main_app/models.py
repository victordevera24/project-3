from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django import forms

RATINGS = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'))


# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # print(f'here is the print {self}')
        return reverse('detail', kwargs={'store_id': self.id})



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    on_sale = models.BooleanField()
    sale_price = models.IntegerField()
    sale_end = models.DateField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.sale_end}"

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_id': self.id})


class WishList(models.Model):
    name = models.CharField(max_length=100)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name
        


class Review(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField(max_length=1000)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_id': self.product.id})


