from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):

  def setUpTestData():
    Recipe.objects.create(name = 'coffee', cooking_time = 3, ingredients = 'coffee, water')

  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    recipe_name_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(recipe_name_label, 'name')

  def test_cooking_time_helptext(self):
    recipe = Recipe.objects.get(id=1)
    recipe_cooking_time = recipe._meta.get_field('cooking_time').help_text
    self.assertEqual(recipe_cooking_time, 'in minutes')