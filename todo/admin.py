from django.contrib import admin
from .models import Task

# Showing on the database in admin panel
class Taskadmin(admin.ModelAdmin):
    list_display=('task', 'is_completed', 'updated_at')
    search_fields = ('task',)

# Register your models here.
admin.site.register(Task, Taskadmin)