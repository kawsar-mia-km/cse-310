from django.shortcuts import render

from products.models import Product

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')


def shop(request):

    products = Product.objects.all()
    return render(request,'shop.html',{
        'products':products,
    })