# Generated by Django 2.2.28 on 2024-02-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
