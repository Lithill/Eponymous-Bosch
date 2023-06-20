from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib import messages


def show_wishlist(request):

    data_wishlist_item = Wishlist.objects.all()
    context = {
        'list_item': data_wishlist_item,
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
    wishlist.wished_item.add(product)
    messages.info(request, "You added this item to your wishlist!")

    return redirect(request.META.get('HTTP_REFERER'))
