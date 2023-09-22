from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipesSearchForm, CreateRecipeForm
import pandas as pd 
from .utils import get_chart


class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe 
  template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe 
  template_name = 'recipes/detail.html'

def home(request):
  return render(request, 'recipes/recipes_home.html')

def create_view(request):
  create_form = CreateRecipeForm(request.POST or None, request.FILES)
  name = None
  cooking_time = None
  genre = None
  ingredients = None
  rating = None
  # pic = None

  if request.method == 'POST':

    try:
      recipe = Recipe.objects.create(
        name = request.POST.get('name'),
        cooking_time = request.POST.get('cooking_time'),
        ingredients = request.POST.get('ingredients'),
      )

      recipe.save()

    except:
      print('Oops...something went wrong')

  context = {
    'create_form': create_form,
    'name': name,
    'cooking_time': cooking_time,
    'genre': genre,
    'ingredients': ingredients,
    'rating': rating,
    # 'pic': pic
  }

  return render(request, 'recipes/create.html', context)

@login_required
def records(request):
  form = RecipesSearchForm(request.POST or None)
  recipe_df = None
  recipe_diff = None
  chart = None
  qs = None

  if request.method == 'POST':
    recipe_diff = request.POST.get('recipe_diff')
    chart_type = request.POST.get('chart_type')

    recipe_diff_data = {'#1': 'Easy', '#2': 'Medium', '#3': 'Intermediate', '#4': 'Hard'}
    recipe_diff = recipe_diff_data[recipe_diff]

    qs = Recipe.objects.all()
    id_searched = []
    
    for obj in qs:
      diff = obj.calculate_difficulty()
      if diff == recipe_diff:
        id_searched.append(obj.id)
    qs = qs.filter(id__in = id_searched)

    if qs:
      recipe_df = pd.DataFrame(qs.values())
      chart = get_chart(chart_type, recipe_df, labels = recipe_df['name'].values)
      recipe_df = recipe_df.to_html()

      for item in qs.values():
        item_id = item['id']
        item_name = item['name']
        recipe_df = recipe_df.replace(
          f'<td>{item_name}</td>',
          f'<td><a href="/recipes/list{item_id}">{item_name}</a></td>'
        )

  context = {
    'form': form,
    'recipe_df': recipe_df,
    'recipe_diff': recipe_diff,
    'chart': chart,
    'qs': qs,
  }
  return render(request, 'recipes/records.html', context)