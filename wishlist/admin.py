from django.contrib import admin
from .models import WaitingList, WishListSaleItem


# Delete this if decide not to use it
class WaitingListAdmin(admin.ModelAdmin):
    readonly_fields = [
        'users',
    ]
    list_display = (
        'product',
    )

    ordering = (
        'users',
    )


admin.site.register(WaitingList, WaitingListAdmin)


class WishListSaleItemAdmin(admin.ModelAdmin):
    list_display = (
        'wishlist',
        'product',
    )


admin.site.register(WishListSaleItem, WishListSaleItemAdmin)
