from django.contrib import admin
from webapp.models import Tracker, Type, Status


# Register your models here.


class TrackerAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_description', 'content', 'type', 'status']

    def type(self, object):
        for type in object.type.all():
            return type
    list_display_links = ['short_description']
    list_filter = ['content']
    search_fields = ['short_description', 'content']
    exclude = []
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Tracker, TrackerAdmin)
admin.site.register(Type)
admin.site.register(Status)


