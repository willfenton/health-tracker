from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class RegisterForm(UserCreationForm, ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username'})
        # self.fields['username'].label = False
        self.fields['email'].widget = forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'Email'})
        # self.fields['email'].label = False
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': "form-control", 'placeholder':'Password'}) 
        # self.fields['password1'].label = False
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password Confirmation'})
        # self.fields['password2'].label = False


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
