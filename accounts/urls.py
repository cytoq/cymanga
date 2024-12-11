from django.urls import path
from .views import home, register, login_view, profile_view, update_profile, delete_account, custom_logout, PasswordResetView, password_reset_complete


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('profile/delete/', delete_account, name='delete_account'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<int:user_id>/', PasswordResetView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', password_reset_complete, name='password_reset_complete'),
]
