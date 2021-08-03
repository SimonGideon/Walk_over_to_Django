from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question


# Create your views here.
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    """output = ','.join([q.question_text for q in latest_question_list])"""
    return render(request, 'index.html', context)


def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not exist")
    return render(request, 'detail.html', {'question': question})
    return HttpResponse("You're looking at the question%s" % question_id)


def results(request, question_id):
    response = "You're looking at the results of questions %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("")
