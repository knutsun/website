from django.contrib import admin
from .models import Contact
from django.contrib.auth.models import Group

admin.site.site_header = 'Gateway Dashboard'

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'date', 'subject')
	list_filter = ('date',)

admin.site.register(Contact, ContactAdmin)
