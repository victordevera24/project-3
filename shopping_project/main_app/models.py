from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Store(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def test(self):
        pass



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    sale_price = models.IntegerField()
    sale_end = models.DateField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} {self.sale_end}"



class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Photo(models.Model):
    url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for product_id: {self.product_id} @{self.url}"
