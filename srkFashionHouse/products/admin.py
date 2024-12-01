from django.contrib import admin
from . models import  Product,RateProduct
from django.contrib import admin
from .models import Product

# Register your models here.

admin.site.register(Product)
admin.site.register(RateProduct)

