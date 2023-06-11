from django.urls import path
from wishlist.views import show_wishlist
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('add_wish_item/', views.add_wish_item, name="add_wish_item"),
]
