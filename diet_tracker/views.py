from django.shortcuts import render
from django.utils import timezone
from .models import Meal
# Create your views here.
def meals_list(request):
    meals=[]
    meals = Meal.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request,'diet_tracker/meals_list.html', {'meals':meals})