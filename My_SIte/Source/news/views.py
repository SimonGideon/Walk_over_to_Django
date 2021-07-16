from urllib import request

from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def year_archive(year=None, *args, **kwargs):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

# Create your views here.
