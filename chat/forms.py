from django import forms
from chat.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username',)

    username = forms.CharField(max_length=50, required=True)

class AuthForm(AuthenticationForm):
    class Meta:
        model=User
        fields = ('username',)

