# Generated by Django 4.2.5 on 2023-09-17 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_description_recipe_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(help_text='separate ingredients with commas', max_length=350),
        ),
    ]