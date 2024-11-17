from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your Basket is empty!')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QM5qRGDazVQqN0sTDENZihnFaiLmhBt6h1nH5KqgjjHsYAa0Piv8SyJ4rf5dqOmmQCPtn1XVQizU4yaCkhirmj100VKLMzHJU',
        'client_secret': 'testing the client secret'
    }

    return render(request, template, context)
