from django import forms
from .models import Product,RateProduct

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'description', 'category']

class RateProductForm(forms.ModelForm):
    class Meta:
        model = RateProduct
        fields = [
            'stars',
        ]