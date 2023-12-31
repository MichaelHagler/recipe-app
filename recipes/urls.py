from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, records, create_view, about_view

app_name = 'recipes'

urlpatterns = [
  path('home/', home, name='home'),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
  path('recipes/search', records, name='records'),
  path('recipes/create/', create_view, name='create'),
  path('recipes/about', about_view, name='about')
]