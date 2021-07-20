from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "Home.html", {})


def contacts(request, *args, **kwargs):

    return render(request, "contacts.html", {})


def about(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me",
        "my_number": "123",
        "my_list": [123, 4675, 376465]
    }
    return render(request, 'about.html', {})
