# Generated by Django 4.1.7 on 2023-05-04 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0019_delete_rewardcatalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sales', models.FloatField()),
                ('profits', models.FloatField()),
                ('transactions', models.IntegerField()),
            ],
        ),
    ]
