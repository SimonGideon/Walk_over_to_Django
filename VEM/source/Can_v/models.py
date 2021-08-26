from django.db import models
from django.db import transaction
import random


# Create your models here.

class AuthRouter:
    route_app_labels = {'auth', 'contenttpes'}

    def deb_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels

        ):
            return True
        return None

    def allow_migrate(self, db, app_lablel, model_name=None, **hints):
        if app_lablel in self.route_app_labels:
            return db == 'auth_db'
        return None


class PrimaryReplicaRouter:
    def dn_for_read(self, mode, **hints):
        return 'primary'

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {'primary', 'replica1', 'replica2'}
        if obj1._state.db in db_set and obj2.state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True


class MyManager(models.Model):
    def get_queryset(self):
        qs = CustomQuerySet(self.model)
        if self._db is not None:
            qs = qs.using(self.db)
        return qs


@transaction.atomic
def viewfunc(request):
    create_parent()
    try:
        with transaction.atomic():
            generate_relationship()
    except IntegrityError:
        handle_exception()
    add_children()
    do_stuff()
    with transaction.atomic():
        do_more_stuff()


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name


class EntryDetails(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    details = models.TextField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)


class AutoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='A')


class EditorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='E')


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=[('A', 'Author'), ('E', 'Editor')])
    people = models.Manager()

    editors = EditorManager()
