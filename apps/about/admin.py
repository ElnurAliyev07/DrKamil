from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from parler.admin import TranslatableAdmin

from .models import (
    About, Association, AboutImage,
    Article, KindofArticles,
    Presentation, PresentationItem,
    WhyThisDr
)


# --- Association ---
@admin.register(Association)
class AssociationAdmin(TranslatableAdmin):
    list_display = ('name',)
    search_fields = ('translations__name',)  # Parler üçün search belə yazılır


# --- AboutImage inline ---
class AboutImageInline(admin.TabularInline):
    model = AboutImage
    extra = 1
    fields = ('image',)


# --- About ---
@admin.register(About)
class AboutAdmin(TranslatableAdmin):
    list_display = ('title', 'image_count')
    search_fields = ('translations__title',)
    inlines = [AboutImageInline]
    filter_horizontal = ('associations',)

    fieldsets = (
        ('Başlıq və təsvir', {
            'fields': ('title', 'description', 'header_image')
        }),
        ('Bio bölməsi', {
            'fields': ('bio_title', 'bio_description')
        }),
        ('Assosiasiyalar', {
            'fields': ('member_association_title', 'associations')
        }),
    )


# --- KindofArticles inline ---
class KindofArticlesInline(admin.TabularInline):
    model = KindofArticles
    extra = 1
    formfield_overrides = {
        forms.CharField: {'widget': CKEditorWidget()},
    }
    fields = ('image', 'caption')


# --- Article ---
@admin.register(Article)
class ArticleAdmin(TranslatableAdmin):
    list_display = ('title', 'header_image')
    search_fields = ('translations__title',)
    inlines = [KindofArticlesInline]


# --- PresentationItem inline ---
class PresentationItemInline(admin.TabularInline):
    model = PresentationItem
    extra = 1
    min_num = 0


# --- Presentation ---
@admin.register(Presentation)
class PresentationAdmin(TranslatableAdmin):
    list_display = ("title", "header_image")
    search_fields = ('translations__title',)
    inlines = [PresentationItemInline]


# --- WhyThisDr ---
@admin.register(WhyThisDr)
class WhyThisDrAdmin(TranslatableAdmin):
    list_display = ('title', 'subtitle', 'header_image')
    search_fields = ('translations__title',)
