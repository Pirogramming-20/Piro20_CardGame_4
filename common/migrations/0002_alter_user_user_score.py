# Generated by Django 4.1 on 2024-01-19 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_score',
            field=models.IntegerField(default=0),
        ),
    ]
