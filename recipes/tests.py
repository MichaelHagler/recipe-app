from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm

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

  def test_difficulty_calculation(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.calculate_difficulty(), 'Easy')

  def test_get_absolute_url(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.get_absolute_url(), '/list/1')

class RecipesSearchFormTest(TestCase):

  def test_form_renders_recipe_diff_input(self):
    form = RecipesSearchForm()
    self.assertIn('recipe_diff', form.as_p())

  def test_form_renders_chart_type_input(self):
    form = RecipesSearchForm()
    self.assertIn('chart_type', form.as_p())

  def test_form_valid_data(self):
    form = RecipesSearchForm(data={'recipe_diff': '#1', 'chart_type': '#2'})
    self.assertTrue(form.is_valid())