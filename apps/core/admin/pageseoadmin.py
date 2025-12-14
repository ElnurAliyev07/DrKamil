from django.contrib import admin
from parler.admin import TranslatableAdmin
from ..models import PageSEO

@admin.register(PageSEO)
class PageSEOAdmin(TranslatableAdmin):
    list_display = ['page_type', 'get_seo_title', 'get_og_title', 'no_index', 'no_follow']
    list_editable = ['no_index', 'no_follow']

    fieldsets = (
        ('Səhifə Məlumatları', {
            'fields': ('page_type',),
        }),
        ('Meta Məlumatları', {
            'fields': ('seo_title', 'seo_description', 'meta_keywords', 'canonical_url'),
        }),
        ('Open Graph', {
            'fields': ('og_title', 'og_description', 'og_image'),
        }),
        ('Brendinq', {
            'fields': ('logo',),
        }),
        ('Robotlar', {
            'fields': ('no_index', 'no_follow'),
        }),
    )

    def get_seo_title(self, obj):
        return obj.safe_translation_getter('seo_title', any_language=True)
    get_seo_title.short_description = 'SEO Title'

    def get_og_title(self, obj):
        return obj.safe_translation_getter('og_title', any_language=True)
    get_og_title.short_description = 'OG Title'
