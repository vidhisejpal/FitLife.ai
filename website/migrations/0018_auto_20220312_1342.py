# Generated by Django 3.1.7 on 2022-03-12 08:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20220312_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet_menu',
            name='diet_breakfast',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
