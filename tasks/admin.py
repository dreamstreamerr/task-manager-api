from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'user', 'status', 'priority', 'due_date', 'created_at')
    list_display_links = ('title',)
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('title', 'description', 'user__username')
