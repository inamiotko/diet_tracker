from django import forms
from .models import Meal
from django.utils import timezone
class UpdateMeal(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('meal', 'calories', 'description')
        