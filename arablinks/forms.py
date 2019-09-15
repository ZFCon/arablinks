from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    user = forms.CharField(label='', max_length=50, widget = 
    forms.TextInput(attrs = {
        'class': "form-control my-2", 
        'placeholder': "User"
        }))
    password = forms.CharField(label='', max_length=100, widget = 
    forms.TextInput(attrs = {
        'class': "form-control my-2", 
        'placeholder': "Password",
        'type': 'password', 
        }))
    def clean(self):
        data = self.cleaned_data
        username = self.cleaned_data.get('user')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            pass
        else:
            raise forms.ValidationError('user or password are wrong.')
        return data

class RegisterForm(forms.Form):
    user = forms.CharField(label='', max_length=50, widget = 
    forms.TextInput(attrs = {
        'class': "form-control my-2", 
        'placeholder': "User"
        }))
    email = forms.EmailField(label='', max_length=50, widget = 
    forms.TextInput(attrs = {
        'class': "form-control my-2", 
        'placeholder': "Email",
        'type':'email',
        }))
    password = forms.CharField(label='', max_length=100, widget = 
    forms.TextInput(attrs = {
        'class': "form-control my-2", 
        'placeholder': "Confirm Password",
        'type': 'password', 
        }))
    password2 = forms.CharField(label='', max_length=100, widget = 
    forms.TextInput(attrs = {
        'class': "form-control my-2", 
        'placeholder': "Password",
        'type': 'password', 
        }))
    def clean_user(self):
        User = get_user_model()
        data = self.cleaned_data["user"]
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('This user are taken.')
        else:
            pass
        return data
    def clean_email(self):
        User = get_user_model()
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('This email are taken.')
        else:
            pass
        return data
    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise forms.ValidationError('Please make the password match.')
        else:
            pass
        return data

    
    
    