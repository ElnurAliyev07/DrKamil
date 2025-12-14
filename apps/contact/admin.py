from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Contact, Consultation


@admin.register(Contact)
class ContactAdmin(TranslatableAdmin):
    list_display = ('title', 'subtitle', 'work_place_title', 'work_place_subtitle', 'header_image')
    search_fields = ('translations__title',)


@admin.register(Consultation)
class ConsultationAdmin(TranslatableAdmin):
    list_display = ('title', 'number_subtitle')
    search_fields = ('translations__title',)
