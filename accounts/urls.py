from django.urls import path
from .views import AccountSettings, index

urlpatterns = [
    path('', index, name='index'),
    path('settings/', AccountSettings.as_view(), name='settings'),
]