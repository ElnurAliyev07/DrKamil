from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline, TranslatableStackedInline
from .models import (
    IntroSection, Services, ServiceItem,
    Faqs, FaqsItem,
    Comment, CommentItem,
    Appointment,
    HeroContent, HeroSection, HeroSectionImages,
    Blog, BlogItem
)

class HeroSectionImagesInline(admin.TabularInline):
    model = HeroSectionImages

@admin.register(HeroSection)
class HeroSectionAdmin(TranslatableAdmin):
    list_display = ('title', 'subtitle')
    inlines = [HeroSectionImagesInline]

@admin.register(HeroContent)
class HeroContentAdmin(TranslatableAdmin):
    list_display = ('title', 'subtitle', 'button_url')


# --- IntroSection ---
@admin.register(IntroSection)
class IntroSectionAdmin(TranslatableAdmin):
    fieldsets = (
        ('Əsas Məlumat', {
            'fields': ('main_word', 'title', 'subtitle', 'image')
        }),
        ('Mətnlər', {
            'fields': ('text1', 'text2')
        }),
        ('Rəqəmlər', {
            'fields': ('num1', 'num2'),
            'description': 'Buraya 23+, 23k+ kimi dəyərləri daxil edə bilərsiniz.'
        }),
    )

# --- Services ---
class ServiceItemInline(TranslatableTabularInline):
    """Servis elementlərinin əsas bölməyə bağlı inlayn formu"""
    model = ServiceItem
    extra = 2  # yeni əlavə form sayı
    max_num = 10  # maksimum element sayı


@admin.register(Services)
class ServicesAdmin(TranslatableAdmin):
    """Əsas servis bölməsi (başlıq, rotate_word, youtube_link)"""
    list_display = ('title', 'rotate_word', 'youtube_link')
    inlines = [ServiceItemInline]


class FaqsItemInline(TranslatableTabularInline):
    """FAQ elementlərinin inlayn forması"""
    model = FaqsItem
    extra = 2
    max_num = 20


@admin.register(Faqs)
class FaqsAdmin(TranslatableAdmin):
    """FAQ əsas bölməsi admin"""
    list_display = ('main_word', 'title', 'description')
    inlines = [FaqsItemInline]


class CommentItemInline(TranslatableTabularInline):
    """CommentItem inlayn redaktəsi"""
    model = CommentItem
    extra = 2
    max_num = 20


@admin.register(Comment)
class CommentAdmin(TranslatableAdmin):
    """Comment əsas bölməsi"""
    list_display = ('main_word', 'title')
    inlines = [CommentItemInline]


class BlogItemInline(TranslatableTabularInline):
    """Blog maddələrinin inlayn redaktəsi"""
    model = BlogItem
    extra = 2
    max_num = 50


@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    """Blog əsas bölməsi"""
    list_display = ('main_word', 'title', 'description')
    inlines = [BlogItemInline]

@admin.register(Appointment)
class AppointmentAdmin(TranslatableAdmin):
    """Qəbul üçün müraciət əsas bölməsi"""
    list_display = ('title', 'photo')
