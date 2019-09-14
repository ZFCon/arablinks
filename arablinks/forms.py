from django import forms
from django.contrib.auth import authenticate

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
    