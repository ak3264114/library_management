# Generated by Django 4.0.1 on 2022-02-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0002_student_password_student_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn_no',
            field=models.CharField(default=123, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=50),
        ),
    ]