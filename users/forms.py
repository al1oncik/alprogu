from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'username_input',
        'placeholder': 'username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password_input',
        'placeholder': 'password',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'user_input',
        'placeholder': 'First name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'user_input',
        'placeholder': 'Last name',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'user_input',
        'placeholder': 'Username',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'user_input',
        'placeholder': 'email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'user_input',
        'placeholder': 'create password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'user_input',
        'placeholder': 'verify password',
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

