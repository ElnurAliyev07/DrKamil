from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from parler.models import TranslatableModel, TranslatedFields


class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.CharField(max_length=255, blank=True, null=True)
    )
    header_image = models.ImageField(upload_to='blog/header/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or "Untitled Blog"

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloqlar"


class BlogItem(TranslatableModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='items')
    translations = TranslatedFields(
        title=models.CharField(max_length=255, blank=True, null=True),
        description=models.CharField(max_length=255, blank=True, null=True),
        tags=models.CharField(max_length=255, blank=True, null=True)
    )
    image = models.ImageField(upload_to='blog/items/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Slug-u yalnız əsas dilin title-ından yarat
        if not self.slug:
            base_title = self.safe_translation_getter('title', any_language=True)
            if base_title:
                self.slug = slugify(base_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or f"Item of {self.blog}"


class BlogDetail(TranslatableModel):
    item = models.OneToOneField(BlogItem, on_delete=models.CASCADE, related_name='detail')
    translations = TranslatedFields(
        subtitle=models.CharField(max_length=255, blank=True, null=True),
        description=RichTextField(default=""),
    )
    header_image = models.ImageField(upload_to='blog_item_details/header/', blank=True, null=True)
    extra_image = models.ImageField(upload_to='blog_item_details/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter(
            'subtitle', any_language=True
        ) or f"Detail of {self.item}"


class BlogDetailSeo(TranslatableModel):
    detail = models.OneToOneField(BlogDetail, on_delete=models.CASCADE, related_name='seo')
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
        verbose_name = "Blog Detail SEO"
        verbose_name_plural = "Blog Detail SEOs"

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
