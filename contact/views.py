from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from .models import ContactForm


def contact(request):
    return render(request, 'contact/contact.html')



