from django import forms
from .models import Product,RateProduct
from django import forms



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


