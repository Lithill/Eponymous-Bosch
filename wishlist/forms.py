from django import forms
from .models import WaitingList
from django.forms.widgets import CheckboxInput


class WaitingListForm(forms.Form):
    sale_alert = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'}),
    )
