# Generated by Django 4.1.7 on 2023-04-20 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewardcatalog',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]