from django.urls import path
from . import views

urlpatterns = [
    path('', views.meals_list, name='meals_list'),
    path('meal/new/', views.new_meal, name='new_meal'),
]