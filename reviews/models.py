from django.db import models



class ReviewsAndRatings(models.Model):
    class Meta:
        verbose_name_plural = "Reviews and Ratings"

    name = models.CharField(max_length=20, null=True, blank=True)
    one_star_rating = models.BooleanField(default=False)
    two_star_rating = models.BooleanField(default=False)
    three_star_rating = models.BooleanField(default=False)
    four_star_rating = models.BooleanField(default=False)
    five_star_rating = models.BooleanField(default=False)
    review = models.TextField(max_length=600, null=True, blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name
