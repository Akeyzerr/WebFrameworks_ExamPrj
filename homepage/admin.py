from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'requirement', 'date_created', 'date_updated', 'created_by',]
    list_filter = ['status',]
    search_fields = ['title', 'implementation', 'created_by__username']
    date_hierarchy = 'date_created'
    fields = ['title', 'requirement', 'implementation', 'status', 'state']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
            obj.save()
        else:
            obj.edited_by = request.user
        obj.save()

admin.site.register(Entry, EntryAdmin)
