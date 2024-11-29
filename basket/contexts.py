from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_AMOUNT:
        if total < settings.LOW_COST_DELIVERY_AMOUNT:
            delivery = total * Decimal
            (settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        else:
            delivery = total * Decimal(settings.HIGH_DELIVERY_PERCENTAGE / 100)

        remaining_for_free_delivery = settings.FREE_DELIVERY_AMOUNT - total
    else:
        delivery = 0
        remaining_for_free_delivery = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'delivery': delivery,
        'remaining_for_free_delivery': remaining_for_free_delivery,
        'free_delivery_amount': settings.FREE_DELIVERY_AMOUNT,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context
