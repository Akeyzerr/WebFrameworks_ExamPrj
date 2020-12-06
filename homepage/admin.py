from django.contrib import admin
from blog.models import *
from homepage.models import *
from users.models import *


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'requirement', 'date_created', 'date_updated', 'created_by', ]
    list_filter = ['status', ]
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


class QuotesAdmin(admin.ModelAdmin):
    list_display = ['quote', 'clean_state']
    list_filter = ['clean_state', ]
    search_fields = ['quote']
    fields = ['quote', 'clean_state']


admin.site.register(Entry, EntryAdmin)
admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Tag)
admin.site.register(PostComment)
