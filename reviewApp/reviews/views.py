from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
	return render(request, 'reviews/home.html',{'title':'Home'})

def about(request):
	return render(request, 'reviews/about.html',{'title':'About'})

def contact(request):
	return render(request, 'reviews/contact.html',{'title':'Contact'})

class ProductListView(ListView):
	model = Product
	template_name = 'reviews/products.html'
	object_context_name = 'products'
	ordering = ['-name']

class ProductDetailView(DetailView):
	model = Product

