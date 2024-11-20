from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
        'email',
        'phone',
        'message',
        'added_info',
        'date',
    )

    fields = (
        'name',
        'email',
        'phone',
        'message',
        'added_info',
        'date',
    )

    list_display = (
        'email',
        'date',
    )

    ordering = ('-date',)


admin.site.register(Contact, ContactAdmin)