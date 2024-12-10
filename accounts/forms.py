# accounts/forms.py

from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Include any fields you want to allow the user to update
