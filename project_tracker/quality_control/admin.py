from django.contrib import admin
from .models import BugReport, FeatureRequest

def create_status_action(status, description):
    @admin.action(description=description)
    def status_action(modeladmin, request, queryset):
        queryset.update(status=status)
    status_action.__name__ = f'set_status_{status}'    
    return status_action

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'project', 'task')}),
        ('Bug Details', {'fields': ('status', 'priority', 'description')}),
        ('Dates', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    actions = [
        create_status_action('New', 'Переместить в статус "Новая"'),
        create_status_action('In_progress', 'Переместить в статус "В работе"'),
        create_status_action('Completed', 'Переместить в статус "Завершена"'),
    ]

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'project', 'task')}),
        ('Request Details', {'fields': ('status', 'priority', 'description')}),
        ('Dates', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)})
    )
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')