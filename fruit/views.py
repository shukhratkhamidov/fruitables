from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def four(request):
    return render(request, '404.html')

def cart(request):
    return render(request, 'cart.html')

def chackout(request):
    return render(request, 'chackout.html')

def shop_detail(request):
    return render(request, 'shop-detail.html')

def shop(request):
    return render(request, 'shop.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')
