# Generated by Django 4.1.3 on 2022-12-09 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_alter_tracker_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='is_deleted',
        ),
    ]