from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'category',
            'sku',
            'image',
            'type',
            'original_artist',
            'style',
            'orientation',
            'imperial',
            'metric',
            'year',
            'orig_url',
            'og_price',
            'discount_percentage',
        ]

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].label = "Enter the product title"
        self.fields['description'].label = "Enter the product description"
        self.fields['category'].label = "Which category is it in?"
        self.fields['sku'].label = "Enter the sku"
        self.fields['image'].label = "Upload the product image"
        self.fields['type'].label = "Print or Poster?"
        self.fields['original_artist'].label = "Who is the original artist?"
        self.fields['style'].label = "What style is the original artwork? \
            I.e. Surrealist"
        self.fields['orientation'].label = "Landscape or Portrait?"
        self.fields['imperial'].label = "Enter the measurements in inches"
        self.fields['metric'].label = "Enter the measurements in mm's"
        self.fields['year'].label = "What year was the original art made?"
        self.fields['orig_url'].label = "Enter an image url of the \
            original artwork"
        self.fields['og_price'].label = "Enter the usual price"
        self.fields['discount_percentage'].label = "What discount percentage \
            would you like to set it to? (Enter '0' if you don't want \
            it on sale)"

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
