# Generated by Django 4.1.3 on 2022-12-06 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_remove_project_tracker_fk_tracker_project_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='project_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='project_fk', to='webapp.project', verbose_name='Project'),
        ),
    ]