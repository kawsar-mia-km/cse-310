from django import forms
from .models import Order

class CustomOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']
