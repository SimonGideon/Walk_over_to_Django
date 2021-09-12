from django.shortcuts import render

from django.http import HttpResponse


def year_archive(request):
    return render(request, "year_archive.html", {})

# Create your views here.
