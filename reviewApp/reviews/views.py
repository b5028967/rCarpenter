from django.shortcuts import render
from .models import Product, Review
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class ReviewDetailView(DetailView):
	model = Review

class ReviewCreateView(LoginRequiredMixin, CreateView):
	model = Review 
	fields = ['product', 'rating', 'review_text', 'date']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Review 
	fields = ['rating', 'review_text', 'date']

	def form_valid(self, form):
		return super().form_valid(form)

	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False


