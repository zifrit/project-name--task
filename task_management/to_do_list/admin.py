from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.UserTask)
class UserTaskAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'name', 'user']
    list_display = ['id', 'name', 'user', 'archive', 'date_create', 'date_update']
    list_editable = ['archive']
    search_fields = ['name', 'user__username']
