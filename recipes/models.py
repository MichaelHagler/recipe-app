from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length=120)
  description = models.TextField(default='If only words were as good as the meal')
  cooking_time = models.FloatField(help_text='in minutes')
  ingredients = models.CharField(max_length=350)
  pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

  def get_absolute_url(self):
    return reverse('recipes:detail', kwargs={'pk': self.pk})

  def __str__(self):
    return str(self.name)