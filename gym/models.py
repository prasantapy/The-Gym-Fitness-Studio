
from django.db import models
#from django.contrib.auth.models import User  #to manage your account
 
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True) #null the value can be null
    emailid = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=15, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.name

class Enquiry(models.Model):
    name = models.CharField(max_length=150,blank=True, null=True)
    mobile = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, blank=True)
    age = models.CharField(max_length=15, blank=True,null=True)

    GENDER_CHOICES=[('Male','Male'),('Female','Female'),('Other','Other')]
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,blank=True,null= True)

    def __str__(self):  #makes your model readable and meaningful
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=150, null=True)
    price = models.CharField(max_length=100, null=True)
    unit = models.CharField(max_length=50, null=True)
    purchasedate = models.DateField(null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=150, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10, null=True)
    plan = models.CharField(max_length=10, null=True)
    joindate = models.DateField(null=True)
    initamount = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=150, null=True)
    amount = models.CharField(max_length=15, null=True)
    duration = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.name
