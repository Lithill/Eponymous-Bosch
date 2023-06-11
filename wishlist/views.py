from django.shortcuts import render
from wishlist.models import UserWishlist


def show_wishlist(request):

    data_wishlist_item = UserWishlist.objects.all()
    context = {
        'list_item': data_wishlist_item,
        'name': 'Ross'
    }

    return render(request, "wishlist.html", context)
