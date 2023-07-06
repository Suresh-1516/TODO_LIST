from django.contrib import admin
from .models import Notes

# admin.site.register(Notes)

@admin.register(Notes)

class NotesAdmin(admin.ModelAdmin):
    list_display = ['id','date']


