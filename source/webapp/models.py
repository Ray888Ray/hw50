from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Status(models.Model):
    status_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Status')

    def __str__(self):
        return self.status_name


class Type(models.Model):
    type_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Type')

    def __str__(self):
        return self.type_name


class Tracker(models.Model):
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='Status')
    type = models.ManyToManyField('webapp.Type', related_name='type', blank=True)
    short_description = models.CharField(max_length=100, null=False, blank=False, verbose_name='Short')
    content = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Content')
    created_at = models.DateField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return f'{self.pk} {self.short_description[:20]}'
