from django.shortcuts import render


def login(request):
    context = {
        
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