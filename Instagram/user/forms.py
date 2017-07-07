from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import InstagramUser


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(
            email=cleaned_data['email'],
            password=cleaned_data['password'],
        )
        if user is None:
            raise forms.ValidationError("Wrong password or login")
        cleaned_data['user'] = user
        return cleaned_data


class UserCreateForm(UserCreationForm):
    class Meta:
        model = InstagramUser
        fields = ["email", "password1", "password2", "username", "first_name", "last_name"]