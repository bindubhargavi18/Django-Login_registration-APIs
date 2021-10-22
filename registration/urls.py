from django.urls import path
from registration import views

urlpatterns = [
    path('registration', views.user_register, name='register'),
    path('login', views.user_login, name='login')

]