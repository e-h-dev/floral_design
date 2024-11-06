from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, to sort and search the products """

    products = Product.objects.all()

    context = {
        "products": product,
    }

    return render(request, 'products/products.html', context)