from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL

# Create your views here.
def redirector(request, shortcode=None):
    return redirect(get_object_or_404(ShortURL, short_code=shortcode).url)