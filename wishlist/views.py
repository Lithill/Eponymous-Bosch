from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib import messages


@login_required
def show_wishlist(request):
    """
    A view to render the user's wishlist
    """
    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, "wishlist.html", context)


@login_required
def add_wish_item(request, product_id):
    """
    Add item to wishlist for user that's logged in
    """

    product = get_object_or_404(Product, pk=product_id)

    # If user had no wishlist, create one
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    # Add item to wishlist
    wishlist.products.add(product)
    messages.info(request, "You added this item to your wishlist!")

    return redirect(request.META.get('HTTP_REFERER'))
