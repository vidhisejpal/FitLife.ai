# Generated by Django 3.1.7 on 2022-03-12 08:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20220312_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet_menu',
            name='diet_dinner',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='diet_menu',
            name='diet_lunch',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='diet_menu',
            name='diet_snacks',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
