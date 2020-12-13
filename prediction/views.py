from django.shortcuts import render
from django_userforeignkey.models.fields import UserForeignKey
from django.contrib.auth.models import User,auth
# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
import pickle
from django.contrib import messages
from .serializers import TestSer
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.contrib import messages
from .models import *
from .forms import  usersForm
import joblib
def signup(request):
    if request.method == 'POST':
        stu = usersForm(request.POST)
        if stu.is_valid():
            user = User.objects.create_user(username=stu.cleaned_data['User_Name'],
                                            password=stu.cleaned_data['Password'],
                                            email=stu.cleaned_data['Email'])

            user.save()
            stu.save()
            return redirect('login')
    else:
        stu = usersForm()
    return render(request,'signup.html',{'form':stu})
def login(request):
    if request.method == 'POST':
        user = User()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        context = {'user':request.user}
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')
@login_required(login_url='login')
def home(request):
	return render(request,'home.html')
@login_required(login_url='login')
def diab_test(request):
	if(request.method=='POST'):
		test=Test()
		test.Pregnancies=request.POST.get('pg',None)
		test.Glucose=request.POST.get('gl',None)
		test.BP=request.POST.get('bp',None)
		test.Skinthickness=request.POST.get('st',None)
		test.Insulin=request.POST.get('ins',None)
		test.BMI=request.POST.get('bmi',None)
		test.Diabetic_pf=request.POST.get('dpf',None)
		test.age=request.POST.get('age',None)
		test.save()
		data=list((request.POST).dict().values())[1:]
		num_data=[float(i) for i in data ]
		df_data=pd.DataFrame([num_data],columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
		model=joblib.load("prediction\knn.pkl")
		final_res=model.predict(df_data)[0]
		print(type(final_res))
		
		if(final_res==0):
			str_res='NON Diabetic'
		else:
			str_res='Diabetic'
		test.user = str(request.user)
		test.Res=str_res
		test.save()
		
        
		
		
		return render(request,'diab_test.html',{'result':str_res})
	else:
		return render(request, 'diab_test.html')

@login_required(login_url='login')
def dia_admit(request):
	if(request.method=='POST'):
		adm=admit()
		adm.no_of_lab_proc=request.POST.get('nop',None)
		adm.no_of_proc=request.POST.get('nol',None)
		adm.no_of_med=request.POST.get('nom',None)
		adm.diag_1=request.POST.get('d1',None)
		adm.diag_2=request.POST.get('d2',None)
		adm.diag_3=request.POST.get('d3',None)
		adm.no_of_diag=request.POST.get('nod',None)
		adm.diabetes_med=request.POST.get('DM',None)
		adm.save()
		data=list((request.POST).dict().values())[1:]
		num_data=[int(i) for i in data ]
		df_data=pd.DataFrame([num_data],columns=['num_lab_procedures','num_procedures','num_medications','diag_1','diag_2','diag_3','number_diagnoses','diabetesMed'])
		model=joblib.load("prediction\knn.pkl")
		final_res=model.predict(df_data)[0]
		print(type(final_res))
		
		if(final_res==0):
			str_res='admit=< 30 days'
		
		else:
			str_res='Discharge'
		adm.user = str(request.user)
		adm.Res=str_res
		adm.save()
		
        
		
		
		return render(request,'readmit.html',{'result':str_res})
	else:
		return render(request, 'readmit.html')


	
@login_required(login_url='login')
def profile(request):
	diabT = Test.objects.filter(user=str(request.user))
	admitT=admit.objects.filter(user=str(request.user))
	return render(request,'profile.html',{'diabT':diabT,'admitT':admitT})
	



class TestView(viewsets.ModelViewSet):
	queryset = Test.objects.all()
	serializer_class = TestSer


