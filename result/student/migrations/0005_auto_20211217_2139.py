# Generated by Django 3.1.1 on 2021-12-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20211217_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='credit',
            field=models.FloatField(),
        ),
    ]
