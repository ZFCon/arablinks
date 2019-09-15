from django.db import models
from .utils import create_code
from .validator import clean_url
from django.contrib.auth.models import User
from django.urls import reverse
from arablinks import settings

# Create your models here.
class ShortURL(models.Model):
    url = models.CharField(max_length = 220, validators = [clean_url])
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=True, blank=True, null=True)
    short_code = models.CharField(max_length = 15, unique = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default = True)
    def __str__(self):
        return str(self.url)
    
    def save(self, *args, **kwargs):
        self.short_code = create_code(self)
        super(ShortURL, self).save(*args, **kwargs)
