from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return render(request, 'contact/contact.html')
        else:
            messages.error(request, 'You have made an error')
            return redirect('contact')
    else:
        contact_form = ContactForm()
    

    template = 'contact/contact.html'

    context = {
        'contact_form': contact_form
    }
    return render(request, template, context)



