# Generated by Django 4.1.3 on 2022-11-25 09:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_tracker_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='short_description',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Short'),
        ),
    ]