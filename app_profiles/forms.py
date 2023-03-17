from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    date_of_birthday = forms.DateField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birthday']


class AuthForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(strip=False, widget=forms.PasswordInput())
