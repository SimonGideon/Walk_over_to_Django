from django.shortcuts import render

from .models import Sales


# Create your views here.
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
