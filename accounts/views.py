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
            login(request, user)  # Automatically log in the user after registration
            return redirect('profile')  # Redirect to profile page after registration
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('profile')  # Redirect to profile page after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


# Profile view (only accessible if logged in)
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
            return redirect('profile')  # Redirect to profile page after saving
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/update_profile.html', {'form': form})


# Account deletion view (only accessible if logged in)
@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # Delete the user account
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')  # Redirect to the home page after account deletion

    return render(request, 'accounts/delete_account.html')


# Custom logout view (logs out the user and redirects to home)
def custom_logout(request):
    if request.method == 'POST':
        logout(request)  # Log out the user
        messages.info(request, 'You have been logged out.')
        return redirect('home')  # Redirect to home after logout

    return render(request, 'accounts/logout.html')  # Show confirmation page for logout


class PasswordResetView(View):
    template_name = 'accounts/password_reset.html'

    def get(self, request, user_id=None):
        form = None
        if user_id:  # For the reset confirmation form
            user = get_user_model().objects.filter(id=user_id).first()
            if not user:
                raise Http404("User not found")
            form = PasswordChangeForm(user=user)
        elif request.user.is_authenticated:
            form = PasswordChangeForm(user=request.user)

        return render(request, self.template_name, {'form': form, 'user_id': user_id})

    def post(self, request, user_id=None):
        if user_id:  # For the reset confirmation
            user = get_user_model().objects.filter(id=user_id).first()
            if not user:
                raise Http404("User not found")
            form = PasswordChangeForm(user=user, data=request.POST)
        else:
            form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, "Password reset successfully")
            return redirect('password_reset_complete')  # Redirect to a confirmation page

        return render(request, self.template_name, {'form': form, 'user_id': user_id})


def password_reset_complete(request):
    return render(request, 'accounts/password_reset_complete.html')
