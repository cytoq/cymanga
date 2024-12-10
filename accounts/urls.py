# accounts/urls.py

from django.urls import path
from .views import register, login_view, profile_view, update_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),  # Ensure this path exists
]