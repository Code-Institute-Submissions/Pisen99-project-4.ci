from django.contrib import admin
from django.urls import path
from . import views
from .views import index_view, signup_view, login_view, resetpassword_view, contact_view, bookings_view, menu_view

# app_name = 'bookings'

urlpatterns = [
    # path('', views.make_booking, name='make_booking'),
    path('', index_view, name='index'),
    path('signup', signup_view, name='signup'),
    path('login', login_view, name='login'),
    path('resetpassword', resetpassword_view, name='resetpassword'),
    path('contact', contact_view, name='contact'),
    path('bookings', bookings_view, name='bookings'),
    path('menu', menu_view, name='menu'),
]
