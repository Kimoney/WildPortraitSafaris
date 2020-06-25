# Generated by Django 3.0.2 on 2020-06-01 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('safaripackages', '0030_auto_20200601_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daynumber',
            name='daydetails',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='daydetails', to='safaripackages.SafariPackages'),
        ),
        migrations.AlterField(
            model_name='safaripackages',
            name='brief_description',
            field=models.TextField(max_length=400),
        ),
    ]