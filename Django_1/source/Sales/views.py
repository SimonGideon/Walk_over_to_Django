from django.shortcuts import render

from .models import Sales
from .forms import SForm


# Create your views here.
def Sales_create_view(request):
    form = SForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "sales.html", context)


def Sales_detail_view(request):
    obj = Sales.objects.get(id=6)
    # context= {
    # 'title': obj.title,
    # 'description': obj.description
    #  }
    context = {
        'object': obj
    }

    return render(request, "Sales/details.html", {})
