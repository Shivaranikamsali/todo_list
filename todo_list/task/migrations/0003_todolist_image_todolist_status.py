# Generated by Django 5.2 on 2025-05-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_todolist_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
