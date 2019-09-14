from django.contrib import admin
from django.urls import path
from .views import index, LoginView, logout_view, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path('register/', RegisterView.as_view(), name='register'),
]
