from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class HeroSection(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        subtitle=models.CharField(max_length=255, blank=True, null=True)
    )

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Bölməsi'


class HeroSectionImages(models.Model):
    hero_section = models.ForeignKey(HeroSection, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='home/hero_section_images/')

    class Meta:
        verbose_name = 'Hero Section Image'
        verbose_name_plural = 'Hero Section Şəkilləri'


class HeroContent(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        subtitle=models.CharField(max_length=255, blank=True, null=True)
    )
    button_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = 'Hero Content'
        verbose_name_plural = 'Hero Contentləri'


class IntroSection(TranslatableModel):
    """Intro bölməsi (Haqqımda)"""
    translations = TranslatedFields(
        main_word=models.CharField(max_length=100, verbose_name="Əsas söz"),
        title=models.CharField(max_length=255, verbose_name="Başlıq"),
        subtitle=models.CharField(max_length=255, blank=True, null=True, verbose_name="Alt başlıq"),
        text1=models.TextField(blank=True, null=True, verbose_name="Mətn 1"),
        text2=models.TextField(blank=True, null=True, verbose_name="Mətn 2"),
    )

    num1 = models.CharField(max_length=20, blank=True, null=True, verbose_name="Rəqəm 1 (məs: 23+)")
    num2 = models.CharField(max_length=20, blank=True, null=True, verbose_name="Rəqəm 2 (məs: 23k+)")

    image = models.ImageField(upload_to='home/intro_section/', blank=True, null=True, verbose_name="Şəkil")

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = "Intro Section"
        verbose_name_plural = "Haqqımda"


from urllib.parse import urlparse, parse_qs

class Services(TranslatableModel):
    """Servis bölməsi (ümumi hissə)"""
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name="Başlıq"),
        rotate_word=models.CharField(max_length=100, verbose_name="Dönən söz"),
    )
    youtube_link = models.URLField(blank=True, null=True, verbose_name="YouTube linki")

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Servislər"

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    @property
    def youtube_id(self):
        """Youtube linkdən video ID çıxarır"""
        if not self.youtube_link:
            return None
        parsed_url = urlparse(self.youtube_link)
        if 'youtu.be' in parsed_url.netloc:
            # qısaldılmış link: https://youtu.be/ID
            return parsed_url.path[1:]  # /ID → ID
        elif 'youtube.com' in parsed_url.netloc:
            # normal link: https://www.youtube.com/watch?v=ID
            query = parse_qs(parsed_url.query)
            return query.get('v', [None])[0]
        return None



class ServiceItem(TranslatableModel):
    """Servis elementləri (alt hissələr)"""
    services = models.ForeignKey(
        Services,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Əlaqəli Servis"
    )

    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name="Başlıq"),
        description=models.TextField(verbose_name="Açıqlama"),
        slug=models.SlugField(unique=True, blank=True, null=True, verbose_name="Slug")
    )

    icon = models.CharField(max_length=100, blank=True, null=True, verbose_name="İkon sinfi (məs: fa-solid fa-star)")

    def save(self, *args, **kwargs):
        if not self.slug:  # əgər slug boşdursa
            base_title = self.safe_translation_getter('title', any_language=True)
            if base_title:
                self.slug = slugify(base_title)  # title-dən slug yaradır
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Service Item"
        verbose_name_plural = "Servis Elementləri"

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)
        

class Faqs(TranslatableModel):
    """FAQ əsas bölməsi"""
    translations = TranslatedFields(
        main_word=models.CharField(max_length=100, verbose_name="Əsas söz"),
        title=models.CharField(max_length=255, verbose_name="Başlıq"),
        description=models.TextField(blank=True, null=True, verbose_name="Təsvir"),
    )
    photo = models.ImageField(upload_to='home/faqs/', blank=True, null=True, verbose_name="Şəkil")

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = "FAQ Bölməsi"
        verbose_name_plural = "FAQ-lar"


class FaqsItem(TranslatableModel):
    """FAQ sual-cavab maddələri"""
    faqs = models.ForeignKey(
        Faqs,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Əlaqəli FAQ"
    )

    translations = TranslatedFields(
        question=models.CharField(max_length=255, verbose_name="Sual"),
        answer=models.TextField(verbose_name="Cavab"),
    )

    def __str__(self):
        return self.safe_translation_getter('question', any_language=True)

    class Meta:
        verbose_name = "FAQ Maddəsi"
        verbose_name_plural = "FAQ Detalları"


class Comment(TranslatableModel):
    """Rəylər bölməsi"""
    translations = TranslatedFields(
        main_word=models.CharField(max_length=100, verbose_name="Əsas söz"),
        title=models.CharField(max_length=255, verbose_name="Başlıq"),
    )
    before_photo = models.ImageField(upload_to='comments/before_after/', blank=True, null=True, verbose_name="Əvvəl şəkli")
    after_photo = models.ImageField(upload_to='comments/before_after/', blank=True, null=True, verbose_name="Sonra şəkli")

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = "Comment Bölməsi"
        verbose_name_plural = "Rəylər"


class CommentItem(TranslatableModel):
    """Rəy maddələri"""
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Əlaqəli Rəy"
    )

    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name="Başlıq"),
        text=models.TextField(verbose_name="Rəy"),
    )
    star = models.PositiveSmallIntegerField(default=5, verbose_name="Ulduz sayı (1-5)")
    patient_name = models.CharField(max_length=255, verbose_name="Xəstə adı")
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name="Vəzifə / Pozisiya")
    patient_photo = models.ImageField(upload_to='comments/patients/', blank=True, null=True, verbose_name="Xəstə şəkli")
    
    def __str__(self):
        return f"{self.patient_name} - {self.safe_translation_getter('title', any_language=True)}"

    class Meta:
        verbose_name = "Rəy Maddəsi"
        verbose_name_plural = "Rəy Detalları"

       
class Blog(TranslatableModel):
    """Blog bölməsi"""
    translations = TranslatedFields(
        main_word=models.CharField(max_length=100, verbose_name="Əsas söz"),
        title=models.CharField(max_length=255, verbose_name="Başlıq"),
        description=models.TextField(blank=True, null=True, verbose_name="Təsvir"),
    )

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = "Blog Bölməsi"
        verbose_name_plural = "Bloglar"


class BlogItem(TranslatableModel):
    """Blog maddələri"""
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Əlaqəli Blog"
    )

    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name="Başlıq"),
        subtitle=models.CharField(max_length=255, blank=True, null=True, verbose_name="Alt başlıq"),
        slug=models.SlugField(unique=True, blank=True, null=True, verbose_name="Slug")
    )
    image = models.ImageField(upload_to='blog/items/', blank=True, null=True, verbose_name="Şəkil")
    post_date = models.DateField(verbose_name="Yayın tarixi")
    writer = models.CharField(max_length=255, verbose_name="Yazıçı adı")
    writer_photo = models.ImageField(upload_to='blog/writers/', blank=True, null=True, verbose_name="Yazıçı şəkli")

    def save(self, *args, **kwargs):
        if not self.slug:  # əgər slug boşdursa
            base_title = self.safe_translation_getter('title', any_language=True)
            if base_title:
                self.slug = slugify(base_title)  # title-dən slug yaradır
        super().save(*args, **kwargs)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = "Blog Maddəsi"
        verbose_name_plural = "Blog Detalları"


class Appointment(TranslatableModel):
    """Qəbul üçün müraciət bölməsi"""
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name="Başlıq")
    )
    photo = models.ImageField(
        upload_to='appointment/',
        blank=True,
        null=True,
        verbose_name="Şəkil"
    )

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Onlayn Konsultasiya"

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)