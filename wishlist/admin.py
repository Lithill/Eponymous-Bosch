from django.contrib import admin
from .models import WaitingList
from .models import Wishlist


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


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'sale_alert_consent']
