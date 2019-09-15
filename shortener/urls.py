from django.urls import path
from .views import redirector

urlpatterns = [
    path("<shortcode>/", redirector, name="link"),
]
