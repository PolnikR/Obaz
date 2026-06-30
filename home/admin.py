from django.contrib import admin
from .models import HomePage, HomePageSectionItem


class HomePageSectionItemInline(admin.TabularInline):
    model = HomePageSectionItem
    extra = 1
    fields = ('section', 'title', 'description', 'order', 'is_active')


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'phone', 'email', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle', 'intro')
    fieldsets = (
        ('Hero', {
            'fields': ('title', 'subtitle', 'intro', 'cta_text', 'cta_url'),
        }),
        ('Kontakt', {
            'fields': ('phone', 'email', 'contact_text'),
        }),
        ('SEO', {
            'fields': ('seo_title', 'meta_description'),
        }),
        ('Publikovanie', {
            'fields': ('is_active',),
        }),
    )
    inlines = [HomePageSectionItemInline]


@admin.register(HomePageSectionItem)
class HomePageSectionItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'page', 'order', 'is_active')
    list_filter = ('section', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_active')
