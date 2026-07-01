from django.contrib import admin
from .models import Services


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'short_title',
        'description',
        'image',
        'order',
        'is_active',
    )
    list_display = ('title', 'short_title', 'has_image', 'order', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'short_title', 'description')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'id')

    @admin.display(boolean=True, description='obrazok')
    def has_image(self, obj):
        return bool(obj.image)
