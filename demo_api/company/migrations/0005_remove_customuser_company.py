# Generated by Django 5.1.1 on 2024-09-06 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_customuser_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='Company',
        ),
    ]
