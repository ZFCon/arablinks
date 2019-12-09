from django import forms

class SettingsForm(forms.Form):
    old_password = forms.CharField(label='', max_length=100, widget = 
    forms.TextInput(attrs = {
        'class': "form-control my-2", 
        'placeholder': "Old Password",
        'type': 'password', 
        }))
    password = forms.CharField(label='', max_length=100, widget = 
    forms.TextInput(attrs = {
        'class': "form-control my-2", 
        'placeholder': "Password",
        'type': 'password', 
        }))
    password2 = forms.CharField(label='', max_length=100, widget = 
    forms.TextInput(attrs = {
        'class': "form-control my-2", 
        'placeholder': "Confirm Password",
        'type': 'password', 
        }))
        
    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise forms.ValidationError('Please make the password match.')
        else:
            pass
        return data

