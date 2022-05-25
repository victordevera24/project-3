from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Store
from .forms import ProductForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#### Define the home view
def home(request):
  return render(request, 'index.html')

def stores_index(request):
  stores = Store.objects.all()
  return render(request, 'stores/index.html', {'stores' : stores})

class StoreCreate(CreateView):
  model = Store
  fields = ['name', 'street', 'city', 'state', 'zip_code']
  # success_url = '/stores/'


def store_detail(request, store_id):
  store = Store.objects.get(id=store_id)
  return render(request, 'stores/detail.html',{'store' : store})


def products_create(request, store_id):
  form = ProductForm(request.POST)
  if form.is_valid():
    new_product = form.save(commit=False)
    new_product.store_id = store_id
    new_product.save()
  return redirect ('products_create')