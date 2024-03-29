# For Making Migrations of New Database :
        # python3 manage.py makemigrations website
        # python3 manage.py migrate


from django.db import models
from datetime import date
from sqlalchemy import null
from ckeditor.fields import RichTextField
# Create your models here.

class User_Info(models.Model):
    user_id = models.AutoField
    user_gender = models.CharField(max_length=50,blank=False,null=False)
    user_focus_area = models.CharField(max_length=100,blank=False,null=False)
    user_name = models.CharField(max_length=500,blank=False,null=False)
    user_email = models.CharField(max_length=100,blank=False,null=False)
    user_age = models.IntegerField(default=0)
    user_blood_group = models.CharField(max_length=50,blank=False,null=False)
    user_height_ft = models.IntegerField(default=0)
    user_height_in = models.IntegerField(default=0)
    user_height = models.FloatField(default=0)
    user_weight = models.FloatField(default=0)
    user_activity_level = models.CharField(max_length=100,blank=False,null=False)
    user_bmi = models.FloatField(default=0)
    user_bmr = models.FloatField(default=0)

    def __str__(self):
        return self.user_email


class User_Exercise_Info(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=500,blank=False,null=False)
    exercise_name = models.CharField(max_length=500,blank=False,null=False)
    exercise_count = models.IntegerField(default=0)
    exercise_duration = models.FloatField(default=0)
    exercise_calorie_burnt = models.FloatField(default=0)
    exercise_weight_loss = models.FloatField(default=0)
    current_time = models.DateTimeField(blank=False,null=False)

    def __str__(self):
        return self.user_name

class Playlist_Check(models.Model):
    user_id = models.AutoField
    user_email = models.CharField(max_length=100,blank=False,null=False)
    exercise_jj = models.IntegerField(default=0)
    exercise_ac = models.IntegerField(default=0)
    exercise_kp = models.IntegerField(default=0)
    exercise_sar = models.IntegerField(default=0)
    exercise_squats = models.IntegerField(default=0)
    exercise_bl = models.IntegerField(default=0)
    exercise_cs = models.IntegerField(default=0)
    current_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user_email

class Diet_Menu(models.Model):
    
    diet_options = (
    ('Choose' ,'Choose'),
    ('Low Carb Diet' ,'Low Carb Diet'),
    ('High Carb Diet','High Carb Diet'),
    ('Keto Diet','Keto Diet'),
    ('Balanced Diet','Balanced Diet'),
    ('Zone Diet','Zone Diet'),
    ('Depletion Diet','Depletion Diet')
    )
    
    diet_food_options = (
    ('Choose' ,'Choose'),
    ('Vegetarian' ,'Vegetarian'),
    ('Non Vegetarian' ,'Non Vegetarian')
    )

    diet_menu_id = models.AutoField
    diet_choice =  models.CharField(max_length=50,choices = diet_options,default = diet_options[0][0],blank=False,null=False)
    diet_food_choice  = models.CharField(max_length=50,choices = diet_food_options,default = diet_food_options[0][0],blank=False,null=False)
    diet_breakfast =  RichTextField(blank=False,null=False)
    diet_lunch = RichTextField(blank=False,null=False)
    diet_dinner = RichTextField(blank=False,null=False)
    diet_snacks = RichTextField(blank=False,null=False)

    