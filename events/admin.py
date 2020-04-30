from django.contrib import admin

from .models import Event


admin.site.site_header = 'Gateway Dashboard'


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('date',)


admin.site.register(Event, EventAdmin)
