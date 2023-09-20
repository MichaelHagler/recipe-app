from django import forms

CHART__CHOICES = (
  ('#1', 'Bar chart'),
  ('#2', 'Pie chart'),
  ('#3', 'Line chart')
)

class RecipesSearchForm(forms.Form):
  chart_type = forms.ChoiceField(choices = CHART__CHOICES)