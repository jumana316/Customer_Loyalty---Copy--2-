# Generated by Django 4.1.7 on 2023-05-11 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0021_delete_sales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdashboard',
            name='date_time',
        ),
    ]
