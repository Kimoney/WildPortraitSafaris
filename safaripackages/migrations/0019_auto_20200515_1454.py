# Generated by Django 3.0.2 on 2020-05-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safaripackages', '0018_auto_20200515_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safaripackages',
            name='days',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='safaripackages',
            name='nights',
            field=models.FloatField(),
        ),
    ]
