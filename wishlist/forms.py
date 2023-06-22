from django import forms
from .models import WaitingList
from .models import WishListSaleItem
from django.forms.widgets import CheckboxInput


# Delete this if decide not to use it
class WaitingListForm(forms.Form):
    sale_alert = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'}),
    )


# CURRENT - Form to request update during a sale
class WishListSaleItemForm(forms.ModelForm):
    class Meta:
        model = WishListSaleItem
        fields = ['wishlist', 'product']
