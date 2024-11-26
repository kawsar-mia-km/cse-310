from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required
from products.models import CartItem
from django.contrib.auth import logout
def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

@login_required
def cart(request):
    """
    Display the user's cart items and calculate the total cost.
    """
    # Get all cart items for the logged-in user
    cart_items = CartItem.objects.filter(user=request.user)

    # Calculate the total price of all items in the cart
    total = sum(item.product.price * item.quantity for item in cart_items)

    # Pass the cart items and total to the template
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'cart.html', context)

def shop(request):
    category = request.GET.get('category')  # Get the selected category from the query parameters
    if category:
        products = Product.objects.filter(category=category)  # Filter products by category
    else:
        products = Product.objects.all()  # Show all products if no category is selected
    return render(request, 'shop.html', {'products': products, 'category': category})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to login page after successful signup
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def LOGOUT(request):
    logout(request)
    return redirect("home")