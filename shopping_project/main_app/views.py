from django.shortcuts import render
from django.http import HttpResponse
from .models import Store

#### Define the home view
def home(request):
  return render(request, 'index.html')

def stores_index(request):
  stores = Store.objects.all()
  return render(request, 'stores/index.html', {'stores' : stores})