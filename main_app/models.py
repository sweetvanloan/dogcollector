from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('S', 'Snack'),
    
)

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'pk': self.id })

    def __str__(self):
        return f"A {self.color} {self.name}"

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
  )

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"