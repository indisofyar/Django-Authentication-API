# Generated by Django 5.1.3 on 2024-11-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_recipe_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
