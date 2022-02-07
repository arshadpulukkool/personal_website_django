from django.shortcuts import render, redirect
from django.http import request
from django.contrib import admin
from django.template import RequestContext

from .models import contacts, personaldetails, signupform
from .forms import personalform
from django.contrib.auth.models import auth
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def personald(request):
    form = personalform(request.POST)
    if form.is_valid():
        form.save()

    context={'personalform': personalform}
    return render(request, 'sample1.html', context)

def homepage(request):
    return render(request, 'website.html')

def education(request):
    return render(request, 'education.html')
def resume(request):
    return render(request, 'resume.html')
def aboutme(request):
    return render(request, 'aboutme.html')
def contact(request):
    if request.method == 'POST':
        c_name = request.POST['name']
        c_email = request.POST['email']
        c_message = request.POST['message']
        data = contacts(name=c_name, email=c_email, message=c_message)
        data.save()
        print("Success")
        return redirect('/app1/home')
    else:
        return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if password1 == password2:
            if signupform.objects.filter(name=name).exists():
                messages.info(request, 'Username already exists')
                print("Username already registered")
                return redirect('/app1/signup')
            elif signupform.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                print("Email already registered")
                return redirect('/app1/signup')
            else:
                res = signupform(name=name, email=email, password=password1)
                res.save()
                print("Successfully Registered")
                return render(request, 'signin.html')
        else:
            messages.info(request, 'Password does not match')
            print("Password is not matching")
        return redirect('/app1/signup')

    else:
        return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']
        if signupform.objects.filter(email=email, password=password).exists():
            return redirect('home/')
        else:
            messages.info(request, 'Email and password does not match')
            return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')

def terms(request):
    return render(request, 'terms.html')