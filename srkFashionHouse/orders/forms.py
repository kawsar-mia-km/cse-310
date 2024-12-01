from django import forms
from .models import Order
from .forms import CustomOrderForm


class CustomOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['field1', 'field2']
