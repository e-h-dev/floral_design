from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your Basket is empty!')
        return redirect(reverse('products'))

    order_form = OrderForm()
    tempalte = 'checkout.checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
