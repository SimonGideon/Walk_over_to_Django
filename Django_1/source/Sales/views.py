from django.shortcuts import render

from .models import Sales
from .forms import SForm, RawSalesForm


# Create your views here.
def Sales_create_view(request):
    my_form = RawSalesForm()
    if request.method == "POST":
        my_form = RawSalesForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "sales.html", context)

# def Sales_create_view(request):
# print(request.GET)
# print(request.POST)
# title = request.POST.get('title')

# context = {}
# return render(request, "sales.html", context)


# def Sales_create_view(request):
# form = SForm(request.POST or None)
# form = SForm()
# if form.is_valid():
# form.save()
# form = SForm()
# context = {
#  'form': form
# }
#  return render(request, "sales.html", context)


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
