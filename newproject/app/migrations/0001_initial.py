# Generated by Django 4.2.7 on 2023-12-18 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id_branch', models.IntegerField(primary_key=10, serialize=False)),
                ('name_branch', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id_faculty', models.IntegerField(primary_key=10, serialize=False)),
                ('name_faculty', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id_student', models.IntegerField(primary_key=10, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name_student', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255, null=True)),
                ('branch', models.CharField(max_length=255, null=True)),
                ('img', models.TextField(default='', null=True)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id_teacher', models.IntegerField(primary_key=10, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name_teacher', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255, null=True)),
                ('branch', models.CharField(max_length=255, null=True)),
                ('img', models.TextField(default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id_project', models.IntegerField(primary_key=10, serialize=False)),
                ('name_project', models.CharField(max_length=255)),
                ('id_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student', verbose_name='id_student')),
                ('id_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teacher', verbose_name='id_teacher')),
            ],
        ),
    ]