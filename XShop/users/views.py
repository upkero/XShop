from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import ChangeAvatarForm, EditProfileForm, UserLoginForm, UserPasswordChangeForm, UserRegistrationForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    
    def get_redirect_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
            return redirect_page
        return reverse_lazy('main:index')
    
    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()
        if user:
            auth.login(self.request, user)
            if session_key:
                forgot_carts = Cart.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                carts = Cart.objects.filter(session_key=session_key)
                carts.update(user=user)
                for cart in carts:
                    cart.session_key = None
                Cart.objects.bulk_update(carts, ['session_key'])
                
            messages.success(self.request, f'Welcome back, {user.username}! You\'re now logged in.')
            return HttpResponseRedirect(self.get_success_url())


class UserRegistrationView(CreateView):
    template_name = 'users/registr.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user:profile')   
    
    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance
        
        if user:
            form.save()
            auth.login(self.request, user)
            if session_key:
                carts = Cart.objects.filter(session_key=session_key)
                carts.update(user=user)
                for cart in carts:
                    cart.session_key = None
                Cart.objects.bulk_update(carts, ['session_key'])
            messages.success(self.request, f'Welcome, {user.username}! Your account has been created and you\'re now logged in.')
            return HttpResponseRedirect(self.success_url)


def forgotpass(request):
    context = {
        
    }
    return render(request, 'users/forgotpass.html', context)


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = ChangeAvatarForm
    success_url = reverse_lazy('user:profile')
    
    def get_object(self, queryset = None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, "Avatar updated successfully.")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = (
            Order.objects.filter(user=self.request.user)
            .prefetch_related(
                Prefetch(
                    'orderitem_set',
                    queryset=OrderItem.objects.select_related('product'),
                )
            )
            .order_by('-id')
        )
        return context


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