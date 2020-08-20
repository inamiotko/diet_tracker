from django.shortcuts import render
from django.utils import timezone
from .models import Meal
from .forms import UpdateMeal
from django.shortcuts import redirect

# Create your views here.
def meals_list(request):
    meals=[]
    meals = Meal.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request,'diet_tracker/meals_list.html', {'meals':meals})

def new_meal(request):
    if request.method=="POST":
        form = UpdateMeal(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            return redirect('meals_list')
    
    else:
        form = UpdateMeal()
        return render(request, 'diet_tracker/meal_edit.html', {'form': form})
   