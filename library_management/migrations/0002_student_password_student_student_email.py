# Generated by Django 4.0.1 on 2022-02-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]
