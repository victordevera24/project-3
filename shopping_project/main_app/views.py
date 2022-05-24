from django.shortcuts import render
from django.http import HttpResponse
from .models import Store, Product
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


class ProductCreate(CreateView):
  model = Product
  fields = ['name', 'price', 'sale_price', 'sale_end' ]