from .models import Contact
from django.contrib import admin


admin.site.site_header = 'Gateway Dashboard'


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'subject')
    list_filter = ('date',)


admin.site.register(Contact, ContactAdmin)
