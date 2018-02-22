from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(AbstractBaseUser):
    name = models.TextField()
    objects = MyUserManager()
    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, name, password=None):
        if not name:
            raise ValueError('Error')
        user = self.model(
            name = name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password):
        user = self.create_user(
            name,
            password,
        )
        user.is_admin = Ture
        user.save(using=self._db)
        return user
