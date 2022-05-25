from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Store, Product
from .forms import ProductForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
import os
import uuid
import boto3


#### Define the home view
def home(request):
  products = Product.objects.all().order_by('-created')
  return render(request, 'index.html', {'products' : products})

def stores_index(request):
  stores = Store.objects.all()
  return render(request, 'stores/index.html', {'stores' : stores})

class StoreCreate(CreateView):
  model = Store
  fields = ['name', 'street', 'city', 'state', 'zip_code']
  # success_url = '/stores/'


def store_detail(request, store_id):
  store = Store.objects.get(id=store_id)
  products = Product.objects.filter(store=store_id)
  return render(request, 'stores/detail.html',{'store' : store, 'products':products})


def new_product(request, store_id):
  form = ProductForm()
  return render(request, 'products/create.html', {'form' : form, 'store' : store_id})

def product_create(request, store_id):
  form = ProductForm(request.POST)
  if form.is_valid():
    new_product = form.save(commit=False)
    new_product.store_id = store_id
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
      s3 = boto3.client('s3')
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      new_product.url = url
    except:
      print('An error occurrd uploading file to S3')
    form.save()
  return redirect('detail', store_id=store_id)

class ProductUpdate(UpdateView):
  model = Product
  fields = ['name', 'price', 'sale_price', 'sale_end']

  # def get_success_url(self):
  #   return reverse_lazy('product_detail', kwargs = {'product_id' : self.object.id})

class ProductDelete(DeleteView):
  model = Product
  success_url = '/home/'

def product_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'products/detail.html', {'product':product})