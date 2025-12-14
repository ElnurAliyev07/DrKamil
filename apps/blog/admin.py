from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline, TranslatableStackedInline
from .models import Blog, BlogItem, BlogDetail, BlogDetailSeo


class BlogDetailSeoInline(TranslatableStackedInline):
    """
    BlogDetailSeo-nu BlogDetail daxilində redaktə etmək üçün dil dəstəyi olan inline form.
    """
    model = BlogDetailSeo
    extra = 0
    fields = (
        'meta_title', 'meta_description', 'meta_keywords',
        'og_title', 'og_description', 'og_image',
        'twitter_title', 'twitter_description', 'twitter_image', 'logo'
    )


class BlogDetailInline(TranslatableStackedInline):
    """
    BlogDetail-i BlogItem daxilində birbaşa redaktə etmək üçün
    dil dəstəyi olan inline form.
    """
    model = BlogDetail
    extra = 0
    fields = ('subtitle', 'description', 'header_image', 'extra_image')
    inlines = [BlogDetailSeoInline]  # BlogDetailSeo-nu BlogDetail içində redaktə etmək üçün


class BlogItemInline(TranslatableTabularInline):
    """
    BlogItem-ləri Blog daxilində redaktə etmək üçün dil dəstəyi olan inline form.
    """
    model = BlogItem
    extra = 0
    fields = ('title', 'description', 'image', 'slug', 'tags')
    readonly_fields = ('slug',)  # Slug avtomatik yaradılır, redaktəyə ehtiyac yoxdur
    show_change_link = True  # BlogItem-in öz səhifəsinə keçid göstər


@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    """
    Əsas Blog modelinin admin paneli – çoxdilli title və description.
    """
    list_display = ('get_title', 'get_description', 'header_image')
    inlines = [BlogItemInline]
    search_fields = ('translations__title', 'translations__description')
    list_per_page = 20  # Səhifədə göstərilən qeydlərin sayı

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True) or "Untitled Blog"
    get_title.short_description = 'Başlıq'

    def get_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True) or "-"
    get_description.short_description = 'Təsvir'


@admin.register(BlogItem)
class BlogItemAdmin(TranslatableAdmin):
    """
    Hər BlogItem-in öz admin səhifəsi (slug + detail inline ilə).
    """
    list_display = ('get_title', 'get_description', 'image', 'get_tags', 'blog', 'slug')
    list_filter = ('blog',)
    search_fields = ('translations__title', 'translations__description', 'slug', 'translations__tags')
    inlines = [BlogDetailInline]
    readonly_fields = ('slug',)  # Slug avtomatik yaradılır
    list_per_page = 20

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True) or "Untitled Item"
    get_title.short_description = 'Başlıq'

    def get_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True) or "-"
    get_description.short_description = 'Təsvir'

    def get_tags(self, obj):
        return obj.safe_translation_getter('tags', any_language=True) or "-"
    get_tags.short_description = 'Teqlər'


@admin.register(BlogDetail)
class BlogDetailAdmin(TranslatableAdmin):
    """
    BlogDetail-ləri ayrıca idarə etmək üçün.
    """
    list_display = ('get_subtitle', 'item')
    search_fields = ('translations__subtitle', 'translations__description')
    inlines = [BlogDetailSeoInline]  # BlogDetailSeo-nu burada da redaktə etmək
    list_per_page = 20

    def get_subtitle(self, obj):
        return obj.safe_translation_getter('subtitle', any_language=True) or "No Subtitle"
    get_subtitle.short_description = 'Alt Başlıq'


@admin.register(BlogDetailSeo)
class BlogDetailSeoAdmin(TranslatableAdmin):
    """
    BlogDetailSeo-nu ayrıca idarə etmək üçün.
    """
    list_display = ('get_meta_title', 'detail')
    search_fields = (
        'translations__meta_title', 'translations__meta_description',
        'translations__og_title', 'translations__twitter_title'
    )
    list_per_page = 20

    def get_meta_title(self, obj):
        return obj.safe_translation_getter('meta_title', any_language=True) or "No Meta Title"
    get_meta_title.short_description = 'Meta Başlıq'