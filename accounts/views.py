from django.shortcuts import render
from .forms import SettingsForm
from django.views import View
from django.contrib.auth.hashers import check_password

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html', locals())

class AccountSettings(View):
    def get(self, request):
        forms = SettingsForm()
        error = forms.non_field_errors
        return render(request, 'accounts/settings.html', locals())
    def post(self, request):
        forms = SettingsForm(request.POST)
        error = forms.non_field_errors
        return render(request, 'accounts/settings.html', locals())