# Generated by Django 4.0.1 on 2022-02-15 13:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_management', '0005_remove_student_admission_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Credit',
        ),
    ]