from django.urls import path
from .views import home, RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
  path('home/', home, name='home'),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
  path('recipes/search', records, name='records')
]