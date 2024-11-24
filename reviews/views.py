from django.shortcuts import render


def reviews(request):
    return render(request, 'reviews/add_review.html')
