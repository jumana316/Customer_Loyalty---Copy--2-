# Generated by Django 4.1.7 on 2023-05-04 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0007_alter_saleanalysis_add_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profitanalysis',
            name='profit',
        ),
    ]
