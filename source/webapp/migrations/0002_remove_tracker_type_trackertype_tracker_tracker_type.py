# Generated by Django 4.1.3 on 2022-11-19 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='type',
        ),
        migrations.CreateModel(
            name='TrackerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackers', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tracker', to='webapp.tracker', verbose_name='Tracker')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type', to='webapp.type', verbose_name='Type')),
            ],
        ),
        migrations.AddField(
            model_name='tracker',
            name='tracker_type',
            field=models.ManyToManyField(blank=True, related_name='type', to='webapp.trackertype'),
        ),
    ]