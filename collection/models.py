from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    

