from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ChangeAvatarForm, EditProfileForm, UserLoginForm, UserRegistrationForm


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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
        
    context = {
        'form': form
    }
    return render(request, 'users/registr.html', context)


def profile(request):
    if request.method == 'POST':
        form = ChangeAvatarForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user:profile')
    else:
        form = ChangeAvatarForm(instance=request.user)
        
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))


def changepass(request):
    context = {
        
    }
    return render(request, 'users/changepass.html', context)


def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = EditProfileForm(instance=request.user)
        
    context = {
        'form': form
    }
    return render(request, 'users/editprofile.html', context)


def forgotpass(request):
    context = {
        
    }
    return render(request, 'users/forgotpass.html', context)