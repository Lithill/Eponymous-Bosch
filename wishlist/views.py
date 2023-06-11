from django.shortcuts import render
from wishlist.models import Wishlist


def show_wishlist(request):

    data_wishlist_item = Wishlist.objects.all()
    context = {
        'list_item': data_wishlist_item,
    }

    return render(request, "wishlist.html", context)
