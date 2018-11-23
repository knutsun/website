from django.contrib import admin
from .models import Event
from django.contrib.auth.models import Group

admin.site.site_header = 'Gateway Dashboard'

class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'date')
	list_filter = ('date',)

admin.site.register(Event, EventAdmin)
