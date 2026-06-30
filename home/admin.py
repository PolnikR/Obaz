from django.contrib import admin
from .models import Services


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_title', 'order', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'short_title', 'description')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'id')
