from django.contrib import admin
from .models import Sermons
from django.contrib.auth.models import Group

admin.site.site_header = 'Gateway Dashboard'

class SermonsAdmin(admin.ModelAdmin):
	list_display = ('title', 'date')
	list_filter = ('date',)

admin.site.register(Sermons, SermonsAdmin)

