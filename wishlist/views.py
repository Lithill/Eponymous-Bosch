from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib.auth.models import User
from .forms import WishlistForm
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
        # If user has no wishlist, create one
        wishlist = Wishlist.objects.create(user=request.user)
        # Set sale_alert_consent to False for the user's wishlist
        wishlist.sale_alert_consent = False
        wishlist.save(update_fields=['sale_alert_consent'])

    page_name = "Wishlist"
    page_description = "See the items you've saved for later"

    context = {
        'wishlist': wishlist,
        'page_name': page_name,
        'page_description': page_description
    }

    return render(request, "wishlist.html", context)


@login_required
def add_wish_item(request, product_id):
    """
    Add item to wishlist for user that's logged in
    """

    product = get_object_or_404(Product, pk=product_id)

    # If user has no wishlist, create one
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    # Add item to wishlist
    wishlist.products.add(product)
    messages.info(request, "You added this item to your wishlist!")

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from the users wishlist
    """
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Remove product from the wishlist
    wishlist.products.remove(product)
    messages.info(request, "The item was removed from your wishlist")

    return redirect(request.META.get('HTTP_REFERER'))


def sale_alert_consent(request, user_id):
    """
    So user can give consent to be emailed,
    if one of their wishlist items goes on sale.
    """
    wishlist = Wishlist.objects.get(user=request.user)
    if request.method == 'POST':
        form = WishlistForm(request.POST, instance=wishlist)
        if form.is_valid():
            form.save()
            messages.info(
                request, "You updated your preference!")
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(
                request, "Sorry there was an error!")
    else:
        form = WishlistForm(instance=wishlist)
    return render(request, 'wishlist.html', {'form': form})
