from django.urls import path
from . import views
from users import views as user_views
from .views import ProductListView, ProductDetailView, ReviewDetailView, ReviewCreateView, ReviewUpdateView

urlpatterns = [
	path('', views.home, name='reviews-home'),
	path('products/', ProductListView.as_view(), name='reviews-products'),
	path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
	path('reviews/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
	path('reviews/add/', ReviewCreateView.as_view(), name='review-create'),
	path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
	path('about/', views.about, name='reviews-about'),
	path('contact/', views.contact, name='reviews-contact'),
	path('register/', user_views.register, name='register'),
	path('profile/', user_views.profile, name='profile'),
]