# Generated by Django 3.0.2 on 2020-03-15 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safaripackages', '0005_safaripackages_telegram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safaripackages',
            name='telegram',
            field=models.TextField(max_length=140),
        ),
    ]