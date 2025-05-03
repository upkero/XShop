from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
        
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        
    }
    return render(request, 'users/registr.html', context)


def profile(request):
    context = {
        
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...


def changepass(request):
    context = {
        
    }
    return render(request, 'users/changepass.html', context)


def editprofile(request):
    context = {
        
    }
    return render(request, 'users/editprofile.html', context)


def forgotpass(request):
    context = {
        
    }
    return render(request, 'users/forgotpass.html', context)