from django.shortcuts import render

# Create your views here.

def create_order(request):
    if request.method == 'POST':
        form = CustomOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = CustomOrderForm()
    return render(request, 'orders/create_order.html', {'form': form})

def order_success(request):
    return render(request, 'orders/order_success.html')


def home(request):
    return None