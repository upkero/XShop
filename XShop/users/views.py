from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import ChangeAvatarForm, EditProfileForm, UserLoginForm, UserPasswordChangeForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            
            session_key = request.session.session_key
            
            if user:
                auth.login(request, user)
                messages.success(request, f'Welcome back, {username}! You\'re now logged in.')
                
                if session_key:
                    carts = Cart.objects.filter(session_key=session_key)
                    carts.update(user=user)
                    for cart in carts:
                        cart.session_key = None
                    Cart.objects.bulk_update(carts, ['session_key'])
                
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
            
            session_key = request.session.session_key
            
            user = form.instance
            auth.login(request, user)
            
            if session_key:
                    carts = Cart.objects.filter(session_key=session_key)
                    carts.update(user=user)
                    for cart in carts:
                        cart.session_key = None
                    Cart.objects.bulk_update(carts, ['session_key'])
                    
            messages.success(request, f'Welcome, {user.username}! Your account has been created and you\'re now logged in.')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
        
    context = {
        'form': form
    }
    return render(request, 'users/registr.html', context)


def forgotpass(request):
    context = {
        
    }
    return render(request, 'users/forgotpass.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ChangeAvatarForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Avatar updated successfully.")
            return redirect('user:profile')
    else:
        form = ChangeAvatarForm(instance=request.user)
    
    orders = (
        Order.objects.filter(user=request.user)
        .prefetch_related(
            Prefetch(
                'orderitem_set',
                queryset=OrderItem.objects.select_related('product'),
            )
        )
        .order_by('-id')
    )
    
    context = {
        'form': form,
        'orders': orders
    }
    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    messages.success(request, f'Goodbye, {request.user.username}! You\'ve been signed out.')
    auth.logout(request)
    return redirect(reverse('main:index'))


@login_required
def changepass(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully.')
            return redirect('user:changepass')
    else:
        form = UserPasswordChangeForm(user=request.user)
    
    
    context = {
        'form': form,
    }
    return render(request, 'users/changepass.html', context)


@login_required
def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return HttpResponseRedirect(reverse('user:editprofile'))
    else:
        form = EditProfileForm(instance=request.user)
        
    context = {
        'form': form
    }
    return render(request, 'users/editprofile.html', context)


@require_POST
@login_required
def delete_account(request):
    
    password = request.POST.get('password')
    
    if not password:
        messages.error(request, 'Password is required')
        return redirect('user:profile')
    
    user = request.user
    
    user_check = auth.authenticate(username=user.username, password=password)
    if not user_check:
        messages.error(request, 'Incorrect password')
        return redirect('user:profile')
    
    user.is_active = False
    user.save()
    logout(request)
    messages.success(request, f'We’re sorry to see you go, { user.username }. Your account has been deactivated.')
    # user.delete()
    return redirect(reverse('main:index'))


def users_cart(request):
    return render(request, 'users/users_cart.html')