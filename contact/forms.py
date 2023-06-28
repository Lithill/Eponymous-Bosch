from django import forms
from .models import Commission


class CommissionForm(forms.ModelForm):

    class Meta:
        model = Commission
        exclude = ['user', 'status']

    def __init__(self, *args, **kwargs):
        super(CommissionForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Enter your name"
        self.fields['email'].label = "Enter your email"
        self.fields['description'].label = "Tell us about what you'd like the finished piece to look like"
        self.fields['dimensions'].label = "What size would you like it to be?"
        self.fields['style'].label = "What style would you like? (E.g. classical / surrealist)"
        self.fields['artist'].label = "Which artist (if any) would you like it to be in the style of?"
        self.fields['framed'].label = "Tick if you'd like it to be framed"
        self.fields['medium'].label = "What medium would you like? (E.g. watercolour / oil on canvas)"
        self.fields['dominant_colours'].label = "Do you have any particular colour-palette or dominant colours in mind?"
