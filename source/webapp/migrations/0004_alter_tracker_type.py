# Generated by Django 4.1.3 on 2022-11-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_tracker_tracker_type_tracker_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='type', to='webapp.type'),
        ),
    ]
