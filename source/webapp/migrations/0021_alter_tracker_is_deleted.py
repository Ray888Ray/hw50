# Generated by Django 4.1.3 on 2022-12-09 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_alter_project_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]