from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from student.models import Student

# Create your models here.

class par(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length = 254)
    stu=models.ManyToManyField(Student)
    emil=models.EmailField(max_length = 254)
    
