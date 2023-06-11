from django.shortcuts import render
from wishlist.models import ItemWishlist


def show_wishlist(request):

    data_wishlist_item = ItemWishlist.objects.all()
    context = {
        'list_item': data_wishlist_item,
        'name': 'Ross'
    }

    return render(request, "wishlist.html", context)
