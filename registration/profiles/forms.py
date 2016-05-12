from django import forms
from models import Profiles
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class SigninForm(forms.Form):
    email = forms.CharField(label='Email',max_length=200)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

class RegisterForm(forms.Form):
    email = forms.CharField(label='Email',max_length=200)
    password = forms.CharField(label='Password', max_length = 200)
    def validate(self):
        try:
            if Profiles.objects.filter(email=self.cleaned_data['email']).exists():
                return False
            else:
                validate_email(self)
                return True
        except ValidationError:
            return False

class ProfileForm(forms.form):
    email = forms.CharField(label='Email',max_length=200)
    password = forms.CharField(label='Password', max_length = 200)
    image = forms.ImageField()
    password = forms.CharField(max_length=200)
    bio = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
