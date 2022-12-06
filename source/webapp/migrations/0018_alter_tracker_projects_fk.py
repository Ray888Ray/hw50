# Generated by Django 4.1.3 on 2022-12-06 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_remove_tracker_project_tracker_projects_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='projects_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects_fk', to='webapp.project', verbose_name='Project'),
            preserve_default=False,
        ),
    ]