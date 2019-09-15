from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Register your models here.
class UserManager(BaseUserManager):
    def create_user(self,username , email=None, phonenumber=None, password=None, is_admin=False, is_staff=False, is_active=True, **extra_fields):
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            username=self.normalize_email(username)
        )
        user.email = email
        user.phonenumber = phonenumber
        user.set_password(password)  # change password to hash
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, phonenumber=None, password=None, is_admin=True, is_staff=True, is_active=True, **extra_fields):
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            username=self.normalize_email(username)
        )
        user.email = email
        user.phonenumber = phonenumber
        user.set_password(password)
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    phonenumder = PhoneNumberField(null=True, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.email

    @staticmethod
    def has_perm(perm, obj=None):
         # "Does the user have a specific permission?"
         # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
         # "Does the user have permissions to view the app `app_label`?"
         # Simplest possible answer: Yes, always
         return True

    @property
    def is_staff(self):
         # "Is the user a member of staff?"
         return self.staff

    @property
    def is_admin(self):
         # "Is the user a admin member?"
         return self.admin

    @property
    def is_active(self):
         # "Is the user active?"
         return self.active