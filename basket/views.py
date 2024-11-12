from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_basket(request):
    """ renders basket contents """

    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ adds items and quantity of items to basket"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'You have Successfully Added more {product.name}, to your Basket')

    else:
        basket[item_id] = quantity
        messages.success(request, f'You have Successfully Added {product.name}, to your Basket')

    request.session['basket'] = basket
    return redirect(redirect_url)

def adjust_basket(request, item_id):
    """ adds items and quantity of items to basket"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'You have Successfully Added more {product.name}, to your Basket')
    else:
        basket.pop(item_id)


    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

def remove_from_basket(request, item_id):
    """ removes items from basket"""

    product = Product.objects.get(pk=item_id)
    try:
        basket = request.session.get('basket', {})
        
        basket.pop(item_id)
        messages.success(request, f'You have Successfully Removed {product.name}, from your Basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing {e}')
        return HttpResponse(status=200)



