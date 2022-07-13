from tabnanny import verbose

# from tkinter import CASCADE
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.core import serializers
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
 title = models.CharField(max_length=50)
 description = models.CharField(max_length=300)
 teacher = models.CharField(max_length=50)
 enrollkey = models.CharField(max_length=50, unique = True)

 class meta:
     verbose_name_plural="1. Courses"

class Student(models.Model):
    sid=models.ForeignKey(User,on_delete=models.CASCADE)
    edc=models.ManyToManyField(Course)




