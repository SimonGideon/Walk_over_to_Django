from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date_published')


class Choice(models.Model):
    question = models.ForeignKey
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
