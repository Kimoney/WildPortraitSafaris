# Generated by Django 3.0.2 on 2020-03-10 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safaripackages', '0002_auto_20200311_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safaripackages',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]