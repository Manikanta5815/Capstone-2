from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey
from datetime import datetime
# Create your models here.
class users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    User_Name = models.CharField(max_length=20) 
    Email = models.CharField(max_length=40) 
    Password  = models.CharField(max_length=20)  
      
    def __str__(self):
        return self.User_Name 

class Test(models.Model):
    
    user = models.CharField(max_length=50,null=True)
    Pregnancies=models.IntegerField(default=0)
    Glucose=models.IntegerField(default=0)
    BP=models.IntegerField(default=0)
    Skinthickness=models.IntegerField(default=0)
    Insulin=models.IntegerField(default=0)
    BMI=models.IntegerField(default=0)
    Diabetic_pf=models.IntegerField(default=0)
    age=models.IntegerField(default=10)
    Res=models.CharField(max_length=10,default='Dia_def')
    Testdate = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return str(self.user)
class admit(models.Model):
    user = models.CharField(max_length=50,null=True)
    no_of_lab_proc=models.IntegerField(default=0)
    no_of_proc=models.IntegerField(default=0)
    no_of_med=models.IntegerField(default=0)
    diag_1=models.IntegerField(default=0)
    diag_2=models.IntegerField(default=0)
    diag_3=models.IntegerField(default=0)
    no_of_diag=models.IntegerField(default=0)
    diabetes_med=models.IntegerField(default=0)
    Res=models.CharField(max_length=10,default='<30')
    Testdate = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return str(self.user)




