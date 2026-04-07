from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Commentaire


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['message']
        widgets = []

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilsateur"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Mot de passe"}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirmer mot de passe"}),
        }

class LoginForm(AuthenticationForm):
    pass