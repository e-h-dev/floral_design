from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from products.models import Product
from .models import ReviewsAndRatings
from .forms import ReviewForm



def reviews(request):

    #product = get_object_or_404(Product, pk=item_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added a review!')
            return redirect('home')
        else:
            messages.error(request, 'Failed to add review. Please check your form is valid')

    else:

        form = ReviewForm

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
