# Generated by Django 4.2.3 on 2023-07-27 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_items', '0002_rename_appetizer_category_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='cuisine',
            name='cuisine',
        ),
    ]
