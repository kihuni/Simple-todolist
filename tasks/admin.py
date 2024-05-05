from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed')
    list_filter = ('completed',)
    search_fields = ('title',)
    
    
admin.site.register(Task)