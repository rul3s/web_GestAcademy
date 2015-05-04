from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    direction = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    telephone = models.CharField(max_length=9)
    email = models.EmailField()
    #students = models.ForeignKey(Student)



class Academy(models.Model):
    name = models.CharField(max_length=50)
    direction = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, blank=True, null=True)
    #students = models.ForeignKey(Student)


'''
class Student(models.Model):
    name = models.CharField()
    direction = models.CharField()
    city = models.CharField()
    telephone = models.CharField(max_length=9)
    email = models.EmailField()
    teachers = models.ForeignKey(Teacher)
'''
