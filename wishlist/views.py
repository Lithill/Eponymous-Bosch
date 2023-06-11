from django.shortcuts import render, redirect
from wishlist.models import Wishlist
from .forms import WishlistForm
from django.contrib.auth.decorators import login_required


def show_wishlist(request):

    data_wishlist_item = Wishlist.objects.all()
    context = {
        'list_item': data_wishlist_item,
    }

    return render(request, "wishlist.html", context)


@login_required
def add_wish_item(request):

    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Successfully added product to wishlist!')
        else:
            messages.error(request, 'Failed to add product to wishlist')
    else:
        form = WishlistForm()

    # template = 'products/product_detail.html'
    context = {'form': form}

    return render(request, template, context)
