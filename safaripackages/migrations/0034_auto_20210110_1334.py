# Generated by Django 3.0.2 on 2021-01-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safaripackages', '0033_auto_20201109_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safaripackages',
            name='category',
            field=models.ManyToManyField(related_name='posts', to='safaripackages.Category'),
        ),
    ]
