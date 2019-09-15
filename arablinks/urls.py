from django.contrib import admin
from django.urls import path, include
from .views import index, LoginView, logout_view, RegisterView
import shortener

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path('register/', RegisterView.as_view(), name='register'),
    path('l/', include(('shortener.urls', 'shortener'), namespace='shortener')),
]
