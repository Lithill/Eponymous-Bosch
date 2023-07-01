from django.urls import path
from . import views
app_name = 'contact'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('commission/<user_id>', views.commission, name='commission'),
    path('my_commissions/', views.my_commissions, name='my_commissions'),
    path(
        'commission_success/',
        views.commission_success,
        name='commission_success'
    ),
]
