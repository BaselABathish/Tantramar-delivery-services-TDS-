from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.homepage, name='test'),
    path('<str:vendor_name>/catalogue', views.vendor_catalogue, name = 'vendor_catalogue')

]
