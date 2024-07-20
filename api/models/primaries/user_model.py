from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    id = models.AutoField(verbose_name = 'ID', primary_key = True, unique = True)
    name = models.CharField(verbose_name = 'Nome', max_length = 255, blank = False)
    email = models.EmailField(verbose_name = 'E-mail', unique = True, blank = False)
    password = models.CharField(verbose_name = 'Senha', max_length = 255, blank = False)
    is_active = models.BooleanField(verbose_name = 'Activo?', default = True)
    is_staff = models.BooleanField(verbose_name = 'Staff?', default = False)
    is_superuser = models.BooleanField(verbose_name = 'Super?', default = False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Registrado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Atualizado em')

    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'usuário: {self.name}'