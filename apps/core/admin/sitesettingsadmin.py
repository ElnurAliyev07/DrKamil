from django.contrib import admin
from django.utils.html import format_html
from parler.admin import TranslatableAdmin
from ..models import SocialLink, SiteLogo, ContactInfo, FooterInfo, Preloader, Sidebar


# --- SocialLink ---
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('get_icon', 'name', 'url')
    list_display_links = ('get_icon', 'name')

    def get_icon(self, obj):
        return f'<i class="{obj.icon_class}" style="font-size:18px;"></i>'
    get_icon.allow_tags = True
    get_icon.short_description = 'İkon'

# --- SiteLogo ---
@admin.register(SiteLogo)
class SiteLogoAdmin(TranslatableAdmin):
    list_display = ('alt_text', 'image_preview')
    search_fields = ('translations__alt_text',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:4px" />', obj.image.url)
        return "-"
    image_preview.short_description = "Logo"


# --- ContactInfo ---
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')
    search_fields = ('phone', 'email', 'address')
    fieldsets = (
        (None, {
            'fields': ('phone', 'email', 'address', 'map_embed')
        }),
    )


# --- FooterInfo ---
@admin.register(FooterInfo)
class FooterInfoAdmin(TranslatableAdmin):
    list_display = ('description_text', 'copyright_text', 'creation_text', 'slide_text', 'creation_url')
    search_fields = (
        'translations__description_text',
        'translations__copyright_text',
        'translations__creation_text',
        'translations__slide_text',
        'creation_url'
    )


# --- Preloader ---
@admin.register(Preloader)
class PreloaderAdmin(TranslatableAdmin):
    list_display = ('display_text', 'image_preview')
    search_fields = ('translations__display_text',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:4px" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preloader Şəkli"


# --- Sidebar ---
@admin.register(Sidebar)
class SidebarAdmin(TranslatableAdmin):
    list_display = ('sidebar_text',)
    search_fields = ('translations__sidebar_text',)
