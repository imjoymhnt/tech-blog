from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.PROTECT)
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=250, default='', blank=False)
    text = models.TextField()
    thumb = models.ImageField(default='default.jpg',blank=True)
    date_added = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.title


class About(models.Model):
    author_image = models.ImageField(blank=True)
    about_content = models.TextField()

class Contact(models.Model):
    contact_text = models.TextField()
    email = models.EmailField(max_length=254, default='')