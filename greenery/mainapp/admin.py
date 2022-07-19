from django.contrib import admin
from .models import *

# Register your models here.

class GreeneryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'photos')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Greenery, GreeneryAdmin)