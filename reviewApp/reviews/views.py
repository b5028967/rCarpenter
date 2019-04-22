from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'reviews/home.html',{'title':'Home'})

def about(request):
	return render(request, 'reviews/about.html',{'title':'About'})

def contact(request):
	return render(request, 'reviews/contact.html',{'title':'Contact'})

def products(request):
	return render(request, 'reviews/products.html',{'title':'Products'})