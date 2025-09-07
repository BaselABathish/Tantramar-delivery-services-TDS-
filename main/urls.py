from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.homepage, name='home'),

    path('register', views.register_view, name = 'register'),
    path('login', views.login_view, name = 'login'),
    path('vendor_register', views.vendor_register, name = 'vendor_register'),
    path('contact', views.contact_view, name = 'contact'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate_account'),

    path('<str:vendor_name>/catalogue', views.vendor_catalogue, name = 'vendor_catalogue'),

]
