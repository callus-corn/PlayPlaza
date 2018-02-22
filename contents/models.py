from django.db import models

from account.models import User


class Content(models.Model):
    title = models.TextField()
    author = models.ForeignKey(User, related_name='content')
