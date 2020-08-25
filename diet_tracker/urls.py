from django.urls import path, include
from django.views.generic import TemplateView
from . import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.meals_list, name='meals_list'),
    path('meal/new/', views.new_meal, name='new_meal'),
    path('logout/', views.logout,  name='logout'),
    path('about/', views.about,  name='about')
     
]
