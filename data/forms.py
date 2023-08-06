from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    # email = forms.EmailField()
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
        
        widgets = {
            'username': forms.TextInput(attrs={
            'class': 'form-control  text-lg h-8 rounded-full px-2 pt-1 border-2 border-black',
            'placeholder': "Username"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control text-lg h-8 rounded-full px-2 pt-1 border-2 border-black',
                'placeholder': "Email"
                }),
            'password1': forms.TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12 text-lg h-8 rounded-full px-2 pt-1 border-2 border-black',
                'type': 'password',
                'name': 'password',
                'placeholder': "Password",
                'id': "id_register_form_password1"
                }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control col-md-7 col-xs-12 text-lg h-8 rounded-full px-2 pt-1 border-2 border-black',
                'placeholder': "Password Confirmation",
                'id': "id_register_form_password2"
                }),
           

        }
          
       