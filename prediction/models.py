from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey
# Create your models here.
class Test(models.Model):
    user = UserForeignKey(auto_user_add=True)
    Pregnancies=models.IntegerField(default=0)
    Glucose=models.IntegerField(default=0)
    BP=models.IntegerField(default=0)
    Skinthickness=models.IntegerField(default=0)
    Insulin=models.IntegerField(default=0)
    BMI=models.IntegerField(default=0)
    Diabetic_pf=models.IntegerField(default=0)
    age=models.IntegerField(default=10)
    Res=models.CharField(max_length=10,default='Dia_def') 
    def __str__(self):
        return str(self.user)
