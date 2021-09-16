from django.shortcuts import render
from django.http import HttpResponse
from.models import Post
# Create your views here.
posts = [
    {
        'author': 'Mark',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jone',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2019'
    },
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
