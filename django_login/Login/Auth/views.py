from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "Auth/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emailaddress = request.POST['emailaddress']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        myuser =User.objects.create_user(username, emailaddress, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()

        messages.success(request, "Your Account has been successfully created")
        return redirect('signin')
    return render(request, "Auth/signup.html")


def signin(request):
    return render(request, "Auth/signin.html")
def signout(request):
    pass
