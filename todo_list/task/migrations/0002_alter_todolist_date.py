# Generated by Django 5.2 on 2025-05-20 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
