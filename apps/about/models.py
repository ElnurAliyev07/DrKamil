from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields


class Association(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255)
    )

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)

    class Meta:
        verbose_name = "Assosiasiya"
        verbose_name_plural = "Assosiasiyalar"


class About(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=RichTextField(blank=True, null=True),

        bio_title=models.CharField(max_length=255),
        bio_description=RichTextField(blank=True, null=True),

        member_association_title=models.CharField(max_length=255),
    )

    associations = models.ManyToManyField(Association, related_name='abouts', blank=True)
    header_image = models.ImageField(upload_to='about/header/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)

    def image_count(self):
        return self.images.count()
    image_count.short_description = "Şəkillər sayı"

    class Meta:
        verbose_name = "Haqqımda"
        verbose_name_plural = "Haqqımda"


class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return f"{self.about.safe_translation_getter('title', any_language=True)} - Image"


class Article(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=RichTextField(blank=True, null=True),
    )
    header_image = models.ImageField(upload_to='article/header/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)

    class Meta:
        verbose_name = "Məqalə"
        verbose_name_plural = "Məqalələr"


class KindofArticles(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='articles/')
    caption = RichTextField(blank=True, null=True)  # Figcaption mətnini CKEditor ilə yazmaq üçün

    def __str__(self):
        return f"{self.article.safe_translation_getter('title', any_language=True)} şəkil"


class Presentation(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=RichTextField(blank=True, null=True),
    )
    header_image = models.ImageField(upload_to='presentation/header/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)

    class Meta:
        verbose_name = "Təqdimat"
        verbose_name_plural = "Təqdimatlar"


class PresentationItem(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE, related_name='items')
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return (self.text[:40] + '...') if self.text else "Element"


class WhyThisDr(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, blank=True, null=True),
        subtitle=models.CharField(max_length=255, blank=True, null=True),
        description=RichTextField(blank=True, null=True),
    )
    header_image = models.ImageField(upload_to='whythisdr/header/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)

    class Meta:
        verbose_name = "Niyə Dr. Kamil?"
        verbose_name_plural = "Niyə Dr. Kamil?"
