from django.contrib import admin
from .models import WaitingList


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
