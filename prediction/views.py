from django.shortcuts import render

from django_userforeignkey.models.fields import UserForeignKey
from django.contrib.auth.models import User
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
from .forms import  CreateUserForm
import joblib
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	data=Test.objects.all()
	print(data)
	return render(request,'test.html',{'data':data})
@login_required(login_url='login')
def test_take(request):
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
		num_data=[int(i) for i in data ]
		df_data=pd.DataFrame([num_data],columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
		model=joblib.load("prediction\knn.pkl")
		final_res=model.predict(df_data)[0]
		print(type(final_res))
		
		if(final_res==0):
			str_res='NON Diabetic'
		else:
			str_res='Diabetic'
		print(str_res)
		
        
		
		test.Res=str_res
		test.save()
		messages.success(request,'patient Status:{}'.format(str_res))
		return render(request,'test_take.html',)
	else:
		return render(request, 'test_take.html')
class TestView(viewsets.ModelViewSet):
	queryset = Test.objects.all()
	serializer_class = TestSer

