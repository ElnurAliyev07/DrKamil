from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields


class Contact(TranslatableModel):
    """
    Əlaqə səhifəsi üçün çoxdilli model
    """
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        subtitle=models.CharField(max_length=255, blank=True, null=True),
        work_place_title=models.CharField(max_length=255, blank=True, null=True, default='İş yeri'),
        work_place_subtitle=models.CharField(max_length=255, blank=True, null=True, default='Çalışdığım xəstəxana'),
    )
    header_image = models.ImageField(upload_to='contact/header_image', blank=True, null=True)

    class Meta:
        verbose_name = 'Əlaqə'
        verbose_name_plural = 'Əlaqə'

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or "Əlaqə"


class Consultation(TranslatableModel):
    """
    Online Konsultasiya səhifəsi üçün çoxdilli model
    """
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        subtitle=RichTextField(default=''),
        description=RichTextField(default=''),
        number_subtitle=models.CharField(max_length=255, blank=True, null=True),
    )

    class Meta:
        verbose_name = 'Online Konsultasiya'
        verbose_name_plural = 'Online Konsultasiya'

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or "Online Konsultasiya"
