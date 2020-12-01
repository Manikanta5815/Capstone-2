from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('prediction', views.TestView)

urlpatterns = [
	path('', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name="home"),
    path('test/', views.test_take, name="test_take"),
	path('api/',include(router.urls)),
	
] 
