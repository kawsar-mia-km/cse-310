
# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomOrderForm


def create_order(request):
    if request.method == 'POST':
        form = CustomOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders:order_list')  # Replace with your success URL
    else:
        form = CustomOrderForm()

    return render(request, 'orders/create_order.html', {'form': form})



def order_success(request):
    return render(request, 'orders/order_success.html')


def home(request):
    return None