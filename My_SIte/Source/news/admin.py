from django.contrib import admin

# Register your models here.
from .models import Reporter, Article
admin.site.register(Reporter)
admin.site.register(Article)
