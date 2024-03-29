# Generated by Django 3.1.7 on 2022-03-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20220309_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet_choice', models.CharField(choices=[('Choose', 'Choose'), ('Low Carb Diet', 'Low Carb Diet'), ('High Carb Diet', 'High Carb Diet'), ('Keto Diet', 'Keto Diet'), ('Balanced Diet', 'Balanced Diet'), ('Zone Diet', 'Zone Diet'), ('Depletion Diet', 'Depletion Diet')], default='Choose', max_length=50)),
                ('diet_food_choice', models.CharField(choices=[('Choose', 'Choose'), ('Vegetarian', 'Vegetarian'), ('Non Vegetarian', 'Non Vegetarian')], default='Choose', max_length=50)),
                ('diet_breakfast', models.TextField(blank=True)),
                ('diet_lunch', models.TextField(blank=True)),
                ('diet_dinner', models.TextField(blank=True)),
                ('diet_snacks', models.TextField(blank=True)),
            ],
        ),
    ]
