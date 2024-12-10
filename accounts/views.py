from django.shortcuts import render

# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from .forms import ProfileForm
from .models import Profile

@login_required
def profile_view(request):
    # This view can render the user profile page
    return render(request, 'accounts/profile.html')
# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('profile')  # Redirect to profile page after registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirect to profile page after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def update_profile(request):
    user = request.user

    # Ensure the user has a profile
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  # Redirect to the profile page
    else:
        user_form = UserChangeForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)

    return render(request, 'accounts/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
