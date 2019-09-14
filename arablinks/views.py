from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'arablinks/index.html', context={})

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        forms = LoginForm()
        return render(request, 'arablinks/login.html', context={'forms': forms})
    def post(self, request):
        forms = LoginForm(request.POST)
        error = forms.non_field_errors
        if forms.is_valid():
            username = str(forms.cleaned_data['user'])
            password = str(forms.cleaned_data['password'])
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'arablinks/login.html', context={'forms': forms, 'error':error})
def logout_view(request):
    logout(request)
    return redirect('index')

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        forms = RegisterForm()
        return render(request, 'arablinks/register.html', context={'forms':forms})
    def post(self, request):
        forms = RegisterForm(request.POST)
        error = forms.non_field_errors
        if forms.is_valid():
            username = str(forms.cleaned_data['user'])
            email = str(forms.cleaned_data['email'])
            password = str(forms.cleaned_data['password'])
            user = User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'arablinks/register.html', context={'forms':forms, 'error':error})