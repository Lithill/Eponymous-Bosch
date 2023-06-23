from django.urls import path
from . import views
app_name = 'contact'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('commission/', views.commission, name='commission'),
    path('my_commissions/', views.my_commissions, name='my_commissions'),
]
