# Generated by Django 3.1.2 on 2020-10-11 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200923_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='profile_picture',
        ),
    ]