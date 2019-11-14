from django.db import models

# Create your models here.
class Marks(models.Model):
    obtained_mark= models.IntegerField()
    total_mark= models.IntegerField()
    subject_name=models.CharField(max_length=100)

class Student(models.Model):
    roll_no = models.TextField()
    name = models.TextField(max_length = 40)
    stud_class = models.TextField()
    department = models.TextField()

class Marksheet(models.Model):
    year=models.IntegerField()
    student=models.OneToOneField(Student,blank=True,on_delete=models.CASCADE)
    sub=models.ManyToManyField(Marks,blank=True)




    
    
    
