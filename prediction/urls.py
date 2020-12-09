from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('prediction', views.TestView)

urlpatterns = [
	path('', views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('diab_test',views.diab_test,name='diab_test'),
	path('dia_admit',views.dia_admit,name='dia_admit'),
    path('profile',views.profile,name='profile'),
	path('api/',include(router.urls)),
	
] 

