from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib import messages
from django.views import View
from django.http import Http404


def home(request):
    return render(request, 'home.html', {
        'is_authenticated': request.user.is_authenticated
    })


# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}!')
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/update_profile.html', {'form': form})


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')

    return render(request, 'accounts/delete_account.html')


def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('home')

    return render(request, 'accounts/logout.html')


class PasswordResetView(View):
    template_name = 'accounts/password_reset.html'

    def get(self, request, user_id=None):
        form = None
        if user_id:
            user = get_user_model().objects.filter(id=user_id).first()
            if not user:
                raise Http404("User not found")
            form = PasswordChangeForm(user=user)
        elif request.user.is_authenticated:
            form = PasswordChangeForm(user=request.user)

        return render(request, self.template_name, {'form': form, 'user_id': user_id})

    def post(self, request, user_id=None):
        if user_id:
            user = get_user_model().objects.filter(id=user_id).first()
            if not user:
                raise Http404("User not found")
            form = PasswordChangeForm(user=user, data=request.POST)
        else:
            form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password reset successfully")
            return redirect('password_reset_complete')

        return render(request, self.template_name, {'form': form, 'user_id': user_id})


def password_reset_complete(request):
    return render(request, 'accounts/password_reset_complete.html')
