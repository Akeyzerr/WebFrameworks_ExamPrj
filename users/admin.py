from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'clean_quote_of_the_day']
    search_fields = ['user']
    fields = ['user', 'image', 'clean_quote_of_the_day']


admin.site.register(Profile, ProfileAdmin)
