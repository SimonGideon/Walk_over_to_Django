from django.shortcuts import render
from django.http import HttpResponse
from forms import Contact


# Create your views here.
def contact(request):
    form = contact()
    return render(request, 'form.html', {'form': form})
