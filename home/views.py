from django.shortcuts import render
from contact.models import Contact

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def privacy(request):
    return render(request, 'home/privacy.html')

def delivery_info(request):

    return render(request, 'home/delivery_info.html')