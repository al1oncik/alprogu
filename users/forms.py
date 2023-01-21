from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'username_input form-control',
        'placeholder': 'username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password_input form-control',
        'placeholder': 'password',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'user_input form-control',
        'placeholder': 'First name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'user_input form-control',
        'placeholder': 'Last name',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'user_input form-control',
        'placeholder': 'Username',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'user_input form-control',
        'placeholder': 'email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'user_input form-control',
        'placeholder': 'create password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'user_input form-control',
        'placeholder': 'verify password',
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

