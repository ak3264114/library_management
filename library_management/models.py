from distutils.command.upload import upload
from email.policy import default
from django import views
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100, blank=False)
    book_img = models.ImageField(upload_to = "asset/book_image/")
    author_name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    about = models.CharField(max_length=500, blank=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.book_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    std = models.CharField(max_length=20)
    credit = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)
