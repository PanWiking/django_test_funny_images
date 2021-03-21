from django.contrib.auth.models import User
from django.db import models


class Funny(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # web = models.FileField()
