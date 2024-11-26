from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy', views.privacy, name='privacy'),
    path('customer_enquiries', views.customer_enquiries, name='customer_enquiries'),
]
