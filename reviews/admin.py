from django.contrib import admin

from django.contrib import admin
from .models import ReviewsAndRatings


class ReviewsAdmin(admin.ModelAdmin):
    
    readonly_fields = (
        'name',
        'one_star_rating',
        'two_star_rating',
        'three_star_rating',
        'four_star_rating',
        'five_star_rating',
        'review',
        'date',
        'time',
    )

    fields = (
        'name',
        'one_star_rating',
        'two_star_rating',
        'three_star_rating',
        'four_star_rating',
        'five_star_rating',
        'review',
        'date',
        'time',
    )

    list_display = (
        'name',
        'review',
        'date',
        'time',
    )

    ordering = ('-date', '-time')


admin.site.register(ReviewsAndRatings, ReviewsAdmin)
