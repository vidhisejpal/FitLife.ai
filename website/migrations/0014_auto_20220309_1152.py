# Generated by Django 3.1.7 on 2022-03-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20220225_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='user_weight',
            field=models.FloatField(default=0),
        ),
    ]