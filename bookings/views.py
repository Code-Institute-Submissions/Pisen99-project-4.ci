from django.shortcuts import render
from .models import Bookings
from bookings.models import Bookings


def make_booking(request):
    pass


def index_view(request):

    return render(request, 'index.html')


def signup_view(request):

    return render(request, 'signup.html')


def login_view(request):

    return render(request, 'login.html')


def resetpassword_view(request):

    return render(request, 'resetpassword.html')


def contact_view(request):

    return render(request, 'contact.html')


def bookings_view(request):

    return render(request, 'bookings.html')


def menu_view(request):

    return render(request, 'menu.html')
