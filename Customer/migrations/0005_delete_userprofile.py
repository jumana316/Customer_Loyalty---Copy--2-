# Generated by Django 4.1.7 on 2023-04-20 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_alter_rewardcatalog_name_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
