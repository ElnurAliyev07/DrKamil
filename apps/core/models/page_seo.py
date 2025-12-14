from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.core.cache import cache

class PageType(models.TextChoices):
    HOME = 'home', 'Ana Səhifə'
    ABOUT = 'about', 'Haqqımızda'
    SERVICES = 'services', 'Xidmətlər (Siyahı Səhifəsi)'
    BLOG = 'blog', 'Blog (Siyahı Səhifəsi)'
    CONTACT = 'contact', 'Əlaqə'
    APPOINTMENT = 'appointment', 'Onlayn Konsultasiya'

class PageSEO(TranslatableModel):
    page_type = models.CharField(
        max_length=50,
        choices=PageType.choices,
        unique=True,
    )

    translations = TranslatedFields(
        seo_title=models.CharField(max_length=255, blank=True, null=True),
        seo_description=models.TextField(blank=True, null=True),
        meta_keywords=models.CharField(max_length=255, blank=True, null=True),
        og_title=models.CharField(max_length=255, blank=True, null=True),
        og_description=models.TextField(blank=True, null=True),
    )

    og_image = models.ImageField(upload_to="seo/og-images/", blank=True, null=True)
    logo = models.ImageField(upload_to="seo/logos/", blank=True, null=True)
    canonical_url = models.URLField(blank=True, null=True)
    no_index = models.BooleanField(default=False)
    no_follow = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Səhifə SEO'
        verbose_name_plural = 'Səhifələr üçün SEO'

    def __str__(self):
        return f"{self.get_page_type_display()}"

    @staticmethod
    def get_seo(page_type, language=None):
        cache_key = f"seo_{page_type}_{language or 'default'}"
        seo = cache.get(cache_key)

        if not seo:
            try:
                if language:
                    seo = PageSEO.objects.language(language).get(page_type=page_type)
                else:
                    seo = PageSEO.objects.get(page_type=page_type)
            except PageSEO.DoesNotExist:
                seo = None

            cache.set(cache_key, seo, 60 * 60)

        return seo