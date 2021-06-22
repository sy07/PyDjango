from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    gender = models.BooleanField(default=False)
    fees = models.IntegerField()

    def __str__(self):
        return self.fname

class Employee(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    gender = models.BooleanField(default=False)
    fees = models.IntegerField()

    def __str__(self):
        return self.fname        

class Contact_us(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    dob = models.CharField(max_length=10)
    mobile = models.IntegerField()

    def __str__(self) :
         return self.fname      