from django.contrib import admin
from webapp.models import Tracker, Type, Status, Project

# Register your models here.

admin.site.register(Tracker)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)


