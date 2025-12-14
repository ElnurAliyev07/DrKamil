from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields


class Innovation(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        subtitle=models.TextField(blank=True, null=True),
        link_title=models.CharField(max_length=255)
    )
    header_image = models.ImageField(upload_to='innovation/header/')

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = "Innovation"
        verbose_name_plural = "Rinoplastika ilə bağlı yeniliklər"


class InnovationItem(TranslatableModel):
    innovation = models.ForeignKey(Innovation, on_delete=models.CASCADE, related_name='items')
    translations = TranslatedFields(
        caption=models.CharField(max_length=255, blank=True, null=True)
    )
    image = models.ImageField(upload_to='innovation/items/')

    def __str__(self):
        return self.safe_translation_getter('caption', any_language=True) or f"Item of {self.innovation}"


class Service(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.CharField(max_length=255, blank=True, null=True)
    )
    header_image = models.ImageField(upload_to='service/header/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Xidmətlər"


class ServiceItem(TranslatableModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='items')
    translations = TranslatedFields(
        title=models.CharField(max_length=255, blank=True, null=True)
    )
    image = models.ImageField(upload_to='service/items/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_title = self.safe_translation_getter('title', any_language=True)
            if base_title:
                self.slug = slugify(base_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or f"Item of {self.service}"

    class Meta:
        verbose_name = "Service Item"
        verbose_name_plural = "Xidmətlərin Detalları"


class ServiceDetail(TranslatableModel):
    item = models.OneToOneField(ServiceItem, on_delete=models.CASCADE, related_name='detail')
    translations = TranslatedFields(
        title=models.CharField(max_length=255, blank=True, null=True),
        subtitle=models.CharField(max_length=255, blank=True, null=True),
        intro_text=RichTextField(default=""),
        description=RichTextField(default="")
    )
    header_image = models.ImageField(upload_to='service_item_details/header/', blank=True, null=True)
    extra_image = models.ImageField(upload_to='service_item_details/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or f"Detail of {self.item}"



class ServiceDetailSeo(TranslatableModel):
    detail = models.OneToOneField(ServiceDetail, on_delete=models.CASCADE, related_name='seo')
    translations = TranslatedFields(
        meta_title=models.CharField(max_length=255, blank=True, null=True),
        meta_description=models.CharField(max_length=255, blank=True, null=True),
        meta_keywords=models.CharField(max_length=255, blank=True, null=True),
        og_title=models.CharField(max_length=255, blank=True, null=True),
        og_description=models.CharField(max_length=255, blank=True, null=True),
        twitter_title=models.CharField(max_length=255, blank=True, null=True),
        twitter_description=models.CharField(max_length=255, blank=True, null=True),
    )
    og_image = models.ImageField(upload_to='blog_item_details/og/', blank=True, null=True)
    twitter_image = models.ImageField(upload_to='blog_item_details/twitter/', blank=True, null=True)
    logo = models.ImageField(upload_to='blog_item_details/logo/', blank=True, null=True)

    class Meta:
        verbose_name = "Service Detail SEO"
        verbose_name_plural = "Service Detail SEOs"

    def get_og_image(self):
        if self.og_image:
            return self.og_image.url
        if self.logo:
            return self.logo.url
        return ''

    def get_twitter_image(self):
        if self.twitter_image:
            return self.twitter_image.url
        if self.logo:
            return self.logo.url
        return ''


class AboutRino(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        subtitle=models.CharField(max_length=255, blank=True, null=True),
        intro_text=RichTextField(default=""),
        description=RichTextField(default="")
    )
    header_image = models.ImageField(upload_to='about_rino/header/', blank=True, null=True)
    extra_image = models.ImageField(upload_to='about_rino/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = "About Rino"
        verbose_name_plural = "Rinoplastika haqqında"
