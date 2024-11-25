from django.contrib import admin
from .models import Product, Category, Reviews


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "description",
        "mini_description",
        "price",
        "image",
    )

    ordering = ('-price',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name"
    )


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rating',
        'review',
        'date',
        'time',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reviews, ReviewsAdmin)