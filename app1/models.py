from django.db import models
# Create your models here.


class personaldetails(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    age = models.CharField(max_length=100)


class contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=200)


class signupform(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

