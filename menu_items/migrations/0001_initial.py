# Generated by Django 4.2.3 on 2023-07-27 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appetizer', models.CharField(max_length=40)),
                ('dessert', models.CharField(max_length=40)),
                ('main_dish', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('american', models.CharField(max_length=40)),
                ('asian', models.CharField(max_length=40)),
                ('mexican', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='menu_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('spicy_level', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu_items.category')),
                ('cuisine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu_items.cuisine')),
            ],
        ),
    ]