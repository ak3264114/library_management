# Generated by Django 4.0.1 on 2022-02-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0003_book_isbn_no_alter_student_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_no',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
