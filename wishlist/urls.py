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
        'sale_alert_consent/<int:user_id>/',
        views.sale_alert_consent,
        name='sale_alert_consent'),
]
