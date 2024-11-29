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
        'time',
    )

    fields = (
        'name',
        'email',
        'phone',
        'message',
        'added_info',
        'date',
        'time',
    )

    list_display = (
        'name',
        'email',
        'date',
        'time',
    )

    ordering = ('-date',)


admin.site.register(Contact, ContactAdmin)
