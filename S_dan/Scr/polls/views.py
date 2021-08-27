from unittest import loader

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import datetime
from .models import Question
from .forms import UploadFileForm


# Create your views here.
def handle_uploaded_file(self):
    pass


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILLES)
        if form.is_valid():
            handle_uploaded_file(request.FILE['file'])
            return HttpResponseRedirect('/success/url')
        else:
            form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})


def current_date(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now %s,</body></html>" % now
    return HttpResponse


def index(request):
    latest_question = Question.objects.order_by('_pub_date')[:5]
    template = loader.get_template('index,html')
    context = {
        'latest_question': latest_question,
    }
    return HttpResponse(template.render(context, request))


def index_i(request):
    return render(request, "Home.html", {})


def contacts(request, *args, **kwargs):
    return render(request, "contacts.html", {})


def about(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me",
        "my_number": "123",
        "my_list": [123, 4675, 376465]
    }
    return render(request, 'about.html', {})


def details(request, question_id):
    return HttpResponse("You're looking at the question%s" % question_id)


def results(request, question_id):
    response = "You're looking at the results of questions %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("")
