# Generated by Django 4.1.3 on 2022-11-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_tracker_type_trackertype_tracker_tracker_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='tracker_type',
        ),
        migrations.AddField(
            model_name='tracker',
            name='type',
            field=models.ManyToManyField(related_name='type', to='webapp.type'),
        ),
        migrations.DeleteModel(
            name='TrackerType',
        ),
    ]
