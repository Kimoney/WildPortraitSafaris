# Generated by Django 3.0.2 on 2020-11-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safaripackages', '0031_auto_20200601_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='daynumber',
            name='location',
            field=models.CharField(blank=True, default=1, max_length=200, null=True),
        ),
    ]