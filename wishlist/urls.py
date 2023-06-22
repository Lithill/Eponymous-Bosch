from django.urls import path
from wishlist.views import show_wishlist
from . import views

app_name = 'wishlist'

urlpatterns = [
    path(
        '',
        show_wishlist,
        name='show_wishlist'),
    path(
        'add_wish_item/<product_id>',
        views.add_wish_item,
        name="add_wish_item"),
    path(
        'remove_from_wishlist/<product_id>',
        views.remove_from_wishlist,
        name='remove_from_wishlist'),
    path(
        'waiting_list/<int:user_id>/<int:product_id>',
        views.waiting_list,
        name='waiting_list'),
    path(
        'wish_list_sale_item',
        views.wish_list_sale_item,
        name='wish_list_sale_item'),
]
