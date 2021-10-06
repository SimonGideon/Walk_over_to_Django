from django.urls import path
from . import views
from users import views as user_views
from .views import PostListView
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('register/', user_views.register, name='register'),
    path('about/', views.about, name='blog-about'),
]
