# Generated by Django 4.1.3 on 2022-12-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_alter_tracker_project_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='finished_at',
            field=models.DateField(auto_now=True, null=True, verbose_name='Finish'),
        ),
    ]
