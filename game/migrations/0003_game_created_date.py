# Generated by Django 4.1 on 2024-01-19 03:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_game_defender_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
