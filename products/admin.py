from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = [
        'on_sale',
        'discounted_price'
    ]
    list_display = (
        'name',
        'sku',
        'category',
        'image',
        'type',
        'original_artist',
        'style',
        'orientation',
        'imperial',
        'metric',
        'year',
        'og_price',
        'discount_percentage',
    )

    ordering = (
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
