from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    return HttpResponse("<h1>Hello World</h1>")


def contact_view(request):
    return HttpResponse("<h1>Contacts Page</h1>")


def about_view(request):
    return HttpResponse("<h1>About Page</h1>")


def social_viw(request):
    return HttpResponse("<h1>Contacts Page</h1>")
