from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    Email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileChangeForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
