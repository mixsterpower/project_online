# Generated by Django 4.2.2 on 2024-02-15 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='password',
        ),
    ]
