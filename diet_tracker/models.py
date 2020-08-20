from django.db import models
from django.utils import timezone
# Create your models here.

class Meal(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    meal = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    
    def submit(self):
        self.date=timezone.now()
        self.save
        
    def __str__(self):
        return self.meal