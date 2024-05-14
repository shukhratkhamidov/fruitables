from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('four/', views.four, name="404-page"),
    path('cart/', views.cart, name="cart-page"),
    path('chackout/', views.chackout, name="chackout-page"),
    path('testimonial/', views.testimonial, name="testimonial-page"),
    path('contact/', views.contact, name="contact-page"),
    path('shopdetail/', views.shop_detail, name="shops-page"),
    path('shop/', views.shop, name="shop-page")
]