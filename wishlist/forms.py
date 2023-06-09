from django import forms
from .models import Wishlist
from django.forms.widgets import CheckboxInput


class WishlistForm(forms.ModelForm):
    sale_alert_consent = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'}),
    )

    class Meta:
        model = Wishlist
        fields = ['sale_alert_consent']
