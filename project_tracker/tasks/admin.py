from django.contrib import admin
from .models import Project, Task

class TaskInLine(admin.TabularInline):
    model = Task
    extra = 0
    field = ('name', 'description', 'assignee', 'status', 'created_at', 'updated_at')
    readonly_field = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    inlines = [TaskInLine]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assignee', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'assignee', 'project')
    search_fields = ('name', 'description')
    list_editable = ('status', 'assignee')
    readonly_fields = ('created_at', 'updated_at')