from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, CartItem
from django.http import JsonResponse



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    return redirect('shop')


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')



def update_quantity(request, cart_item_id):

    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
        new_quantity = int(request.POST.get('quantity', 1))
        if new_quantity > 0:
            cart_item.quantity = new_quantity
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('cart')
    return JsonResponse({'error': 'Invalid request method'}, status=400)