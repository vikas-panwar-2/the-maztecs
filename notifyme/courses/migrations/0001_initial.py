# Generated by Django 3.1.2 on 2020-12-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=100)),
                ('secret_key', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'course_table',
            },
        ),
    ]
