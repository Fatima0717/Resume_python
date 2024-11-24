from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    ordering = ['-created_at']