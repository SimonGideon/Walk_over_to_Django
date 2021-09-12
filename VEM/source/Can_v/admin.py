from django.contrib import admin
from .models import Entry
from django.contrib import admin


# Specialize the multi-db admin objects for use with specific models.
class BookInline(MultiDBTabularInline):
    model = Book


class PublisherAdmin(MultiDBModelAdmin):
    inlines = [BookInline]


admin.site.register(Author, MultiDBModelAdmin)
admin.site.register(Publisher, PublisherAdmin)

admin.site.register(Entry)

# Register your models here.
