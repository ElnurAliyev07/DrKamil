from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline, TranslatableStackedInline
from .models import Innovation, InnovationItem, Service, ServiceItem, ServiceDetail, ServiceDetailSeo, AboutRino


# --- ServiceDetailSeo Inline ---
class ServiceDetailSeoInline(TranslatableStackedInline):
    """
    ServiceDetailSeo-nu ServiceDetail daxilində redaktə etmək üçün dil dəstəyi olan inline form.
    """
    model = ServiceDetailSeo
    extra = 0
    fields = (
        'meta_title', 'meta_description', 'meta_keywords',
        'og_title', 'og_description', 'og_image',
        'twitter_title', 'twitter_description', 'twitter_image', 'logo'
    )


# --- Innovation ---
class InnovationItemInline(TranslatableTabularInline):
    """
    InnovationItem-ləri Innovation daxilində redaktə etmək üçün dil dəstəyi olan inline form.
    """
    model = InnovationItem
    fields = ('caption', 'image')
    extra = 0  # Boş formaların sayını 0 etdik ki, avtomatik boş form əlavə olunmasın
    show_change_link = True  # InnovationItem-in öz səhifəsinə keçid


@admin.register(Innovation)
class InnovationAdmin(TranslatableAdmin):
    """
    Innovation modelinin admin paneli – çoxdilli title, subtitle və link_title.
    """
    list_display = ('get_title', 'get_subtitle', 'get_link_title', 'header_image')
    inlines = [InnovationItemInline]
    search_fields = ('translations__title', 'translations__subtitle', 'translations__link_title')
    list_per_page = 20

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True) or "Untitled Innovation"
    get_title.short_description = 'Başlıq'

    def get_subtitle(self, obj):
        return obj.safe_translation_getter('subtitle', any_language=True) or "-"
    get_subtitle.short_description = 'Alt Başlıq'

    def get_link_title(self, obj):
        return obj.safe_translation_getter('link_title', any_language=True) or "-"
    get_link_title.short_description = 'Link Başlığı'


# --- Service ---
class ServiceDetailInline(TranslatableStackedInline):
    """
    ServiceDetail-i ServiceItem daxilində redaktə etmək üçün dil dəstəyi olan inline form.
    """
    model = ServiceDetail
    fields = ('title', 'subtitle', 'intro_text', 'description', 'header_image', 'extra_image')
    extra = 0
    inlines = [ServiceDetailSeoInline]  # ServiceDetailSeo-nu ServiceDetail içində redaktə etmək


class ServiceItemInline(TranslatableTabularInline):
    """
    ServiceItem-ləri Service daxilində redaktə etmək üçün dil dəstəyi olan inline form.
    """
    model = ServiceItem
    fields = ('title', 'image', 'slug')
    extra = 0
    readonly_fields = ('slug',)  # Slug avtomatik yaradılır
    show_change_link = True  # ServiceItem-in öz səhifəsinə keçid


@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    """
    Service modelinin admin paneli – çoxdilli title və description.
    """
    list_display = ('get_title', 'get_description', 'header_image')
    inlines = [ServiceItemInline]
    search_fields = ('translations__title', 'translations__description')
    list_per_page = 20

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True) or "Untitled Service"
    get_title.short_description = 'Başlıq'

    def get_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True) or "-"
    get_description.short_description = 'Təsvir'


@admin.register(ServiceItem)
class ServiceItemAdmin(TranslatableAdmin):
    """
    ServiceItem-in öz admin səhifəsi (slug + detail inline ilə).
    """
    list_display = ('get_title', 'service', 'slug', 'image')
    list_filter = ('service',)
    search_fields = ('translations__title', 'slug')
    inlines = [ServiceDetailInline]
    readonly_fields = ('slug',)  # Slug avtomatik yaradılır
    list_per_page = 20

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True) or "Untitled Service Item"
    get_title.short_description = 'Başlıq'


@admin.register(ServiceDetail)
class ServiceDetailAdmin(TranslatableAdmin):
    """
    ServiceDetail-ləri ayrıca idarə etmək üçün.
    """
    list_display = ('get_title', 'get_subtitle', 'item')
    search_fields = ('translations__title', 'translations__subtitle', 'translations__intro_text')
    inlines = [ServiceDetailSeoInline]  # ServiceDetailSeo-nu burada da redaktə etmək
    list_per_page = 20

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True) or "No Title"
    get_title.short_description = 'Başlıq'

    def get_subtitle(self, obj):
        return obj.safe_translation_getter('subtitle', any_language=True) or "No Subtitle"
    get_subtitle.short_description = 'Alt Başlıq'


@admin.register(ServiceDetailSeo)
class ServiceDetailSeoAdmin(TranslatableAdmin):
    """
    ServiceDetailSeo-nu ayrıca idarə etmək üçün.
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


# --- AboutRino ---
@admin.register(AboutRino)
class AboutRinoAdmin(TranslatableAdmin):
    """
    AboutRino modelinin admin paneli – çoxdilli title, subtitle, intro_text və description.
    """
    list_display = ('get_title', 'get_subtitle', 'header_image')
    search_fields = ('translations__title', 'translations__subtitle', 'translations__intro_text')
    list_per_page = 20

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True) or "Untitled About Rino"
    get_title.short_description = 'Başlıq'

    def get_subtitle(self, obj):
        return obj.safe_translation_getter('subtitle', any_language=True) or "-"
    get_subtitle.short_description = 'Alt Başlıq'