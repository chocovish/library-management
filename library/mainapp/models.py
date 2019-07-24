from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# Create your models here.


class User(AbstractUser):
    choices = (('CSE','CSE'),('ECE','ECE'))
    phone = models.CharField(max_length=15)
    roll = models.CharField(max_length=20)
    stream = models.CharField(max_length=5, choices=choices)
    year = models.CharField(max_length=4)
    verified = models.BooleanField(default=False)


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=16)
    borrower = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    borrow_date = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name +" by " + self.author