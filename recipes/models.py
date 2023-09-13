from django.db import models

# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length=120)
  cooking_time = models.FloatField(help_text='in minutes')
  ingredients = models.CharField(max_length=350)

  def get_absolute_url(self):
    return reverse('recipes:detail', kwargs={'pk': self.pk})

  def __str__():
    return str(self.name)