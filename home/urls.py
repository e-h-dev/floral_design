from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy', views.privacy, name='privacy'),
    path('delivery_info', views.delivery_info, name='delivery_info'),
]
