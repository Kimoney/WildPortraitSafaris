# Generated by Django 3.0.2 on 2020-05-15 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safaripackages', '0016_auto_20200515_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='safaripackages',
            name='days',
        ),
        migrations.RemoveField(
            model_name='safaripackages',
            name='nights',
        ),
    ]
