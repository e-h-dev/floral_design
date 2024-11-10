from decimal import Decimal
from django.conf import settings

def basket_contents(requst):

    basket_items = []
    total = 0
    products_count = 0

    if total < settings.FREE_DELIVERY_AMOUNT:
        if total < 50:
            delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
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
    }

    return context