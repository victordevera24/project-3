from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Store, Product, Review, WishList
from .forms import ProductForm, WishListForm, ReviewForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
import os
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#### Define the home view
def home(request):
  products = Product.objects.all().order_by('-created')
  return render(request, 'index.html', {'products' : products})

@login_required
def stores_index(request):
  stores = Store.objects.all()
  return render(request, 'stores/index.html', {'stores' : stores})

class StoreCreate(LoginRequiredMixin, CreateView):
  model = Store
  fields = ['name', 'street', 'city', 'state', 'zip_code']
  # success_url = '/stores/'

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class StoreUpdate(LoginRequiredMixin, UpdateView):
  model = Store
  fields = ['name', 'street', 'city', 'state', 'zip_code']

class StoreDelete(LoginRequiredMixin, DeleteView):
  model = Store
  success_url = '/stores/'

@login_required
def store_detail(request, store_id):
  store = Store.objects.get(id=store_id)
  products = Product.objects.filter(store=store_id)
  
  return render(request, 'stores/detail.html',{'store' : store, 'products':products})

@login_required
def new_product(request, store_id):
  form = ProductForm()
  return render(request, 'products/create.html', {'form' : form, 'store' : store_id})

@login_required
def product_create(request, store_id):
  form = ProductForm(request.POST)
  if 'on_sale' in request.POST:
    print("yippee kay ay")
  if form.is_valid():
    new_product = form.save(commit=False)
    new_product.store_id = store_id
    new_product.user_id = request.user.id
    if 'on_sale' in request.POST:
      new_product.on_sale = True
    else:
      new_product.on_sale = False
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
      print('An error occurred uploading file to S3')
    form.save()
  return redirect('detail', store_id=store_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
  
    form = UserCreationForm(request.POST)
    if form.is_valid():
      
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProductUpdate(LoginRequiredMixin, UpdateView):
  model = Product
  fields = ['name', 'price', 'sale_price', 'sale_end']

class ProductDelete(LoginRequiredMixin, DeleteView):
  model = Product
  success_url = '/stores/'

@login_required
def product_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  reviews = Review.objects.filter(product=product_id)
  wishlist = WishList.objects.filter(users=request.user).exclude(products__id = product_id)
  wishlists_in_use = WishList.objects.filter(users=request.user, products__id = product_id)
  return render(request, 'products/detail.html', {'product':product, 'reviews':reviews, 'wishlists':wishlist, "usedwl":wishlists_in_use})

@login_required
def new_wishlist(request, product_id):
  form = WishListForm()
  return render(request, 'wishlists/create.html', {'form' : form, 'product_id' : product_id})

@login_required
def wishlist_create(request, product_id):
  form = WishListForm(request.POST)
  if form.is_valid():
    new_wishlist = form.save(commit=False)
    new_wishlist.users_id = request.user.id
    form.save()
  return redirect('product_detail', product_id=product_id)

@login_required
def assoc_product(request, product_id):
  WishList.objects.get(id=request.POST['id']).products.add(product_id) 
  return redirect('product_detail', product_id=product_id)


@login_required
def new_review(request, product_id):
  form = ReviewForm()
  return render(request, 'reviews/create.html', {'form' : form, 'product' : product_id})


@login_required
def review_create(request, product_id):
  product = Product.objects.get(id=product_id)
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.product = product
    new_review.user = request.user
    new_review.save()
    return redirect('product_detail', product_id = product_id)
  else:# redirect back to the user page with errors
    return render(request, 'reviews/create.html', {'form':form, 'product': product_id})

class ReviewUpdate(LoginRequiredMixin, UpdateView):
  model = Review
  fields = ['title', 'review', 'rating']

class ReviewDelete(LoginRequiredMixin, DeleteView):
  model = Review
  def get_success_url(self, **kwargs):
        return reverse('product_detail', args=(self.object.product.id,))

@login_required
def wishlists_index(request):
  wishlists = WishList.objects.filter(users=request.user)
  return render(request, 'wishlists/index.html', {'wishlists' : wishlists, 'user': request.user})

@login_required
def wishlists_detail(request, wishlist_id):
  wishlist = WishList.objects.get(id=wishlist_id)
  products = wishlist.products.all()
  return render(request, 'wishlists/detail.html', {'wishlist' : wishlist, 'products' : products})

def test(request):
  return render (request, 'stores/test.html')

