from django.db import models


# Create your models here.
class Sales(models.Model):
    title = models.CharField(max_length=120)  # max length requires
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=True) # null=true or default value
