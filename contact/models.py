from django.db import models



class ContactUs(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(max_length=600, null=True, blank=True)
    added_info = models.TextField(max_length=600, null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__():
        return self.email
