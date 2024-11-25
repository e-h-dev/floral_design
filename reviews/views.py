from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from products.models import Product
from .models import ReviewsAndRatings
from .forms import ReviewForm

# def see_reviews(request):

#     reviews = ReviewsAndRatings.objects.all()

#     context = {
#         'reviews': reviews,
#     }

#     return render(request, 'reviews/add_review.html', context)

def reviews(request):

    #product = get_object_or_404(Product, pk=item_id)
    see_reviews = ReviewsAndRatings.objects.all()
    
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
        'see_reviews': see_reviews,
    }

    return render(request, template, context)
