from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class SocialLink(models.Model):
    SOCIAL_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('twitter', 'X (Twitter)'),
        ('youtube', 'YouTube'),
        ('whatsapp', 'WhatsApp'),
        ('tiktok', 'TikTok'),
        ('telegram', 'Telegram'),
    ]

    ICON_CLASSES = {
        'linkedin': 'fa-brands fa-linkedin',
        'instagram': 'fa-brands fa-instagram',
        'facebook': 'fa-brands fa-facebook-f',
        'twitter': 'fa-brands fa-x-twitter',
        'youtube': 'fa-brands fa-youtube',
        'whatsapp': 'fa-brands fa-whatsapp',
        'tiktok': 'fa-brands fa-tiktok',
        'telegram': 'fa-brands fa-telegram',
    }

    name = models.CharField('Sosial şəbəkə', max_length=50, choices=SOCIAL_CHOICES)
    url = models.URLField('URL', blank=True)

    class Meta:
        verbose_name = 'Sosial Media Linki'
        verbose_name_plural = 'Sosial Media Linkləri'

    def __str__(self):
        return dict(self.SOCIAL_CHOICES).get(self.name, self.name)

    @property
    def icon_class(self):
        return self.ICON_CLASSES.get(self.name, '')


class SiteLogo(TranslatableModel):
    translations = TranslatedFields(
        alt_text=models.CharField(
            max_length=100,
            verbose_name='Alt mətn',
            blank=True
        )
    )
    image = models.ImageField(
        upload_to='logos/',  
        verbose_name='Logo Şəkli'
    )

    class Meta:
        verbose_name = 'Sayt Logo'
        verbose_name_plural = 'Logo'

    def __str__(self):
        return self.safe_translation_getter('alt_text', any_language=True) or f"Logo #{self.pk}"


class ContactInfo(models.Model):
    phone = models.CharField(max_length=50, verbose_name="Telefon Nömrəsi", blank=True)
    email = models.EmailField(verbose_name="E-poçt", blank=True)
    address = models.CharField(
        max_length=250,
        verbose_name="Ünvan",
        blank=True,
        default="Atatür prospekti 1010"
    )
    map_embed = models.TextField(
        verbose_name="Google Maps Embed URL / iframe",
        blank=True,
        help_text="Bütün iframe kodunu və ya embed linkini buraya yapışdırın"
    )

    class Meta:
        verbose_name = "Əlaqə Məlumatı"
        verbose_name_plural = "Əlaqə Məlumatları"

    def __str__(self):
        return f"{self.phone or ''} | {self.email or ''}".strip(" |")


class FooterInfo(TranslatableModel):
    translations = TranslatedFields(
        description_text=models.TextField(
            verbose_name="Footer Təsviri",
            blank=True,
            default="Qulaq-burun-boğaz və baş-boyun cərrahiyyəsi uzmanı, Avropa sertifikatlı üz plastik cərrah və otorinolarinqoloq"
        ),
        copyright_text=models.CharField(
            max_length=200,
            verbose_name="Footer Mətni",
            blank=True,
            default="© 2025 Dr. Kamil Cəfərov"
        ),
        creation_text=models.CharField(
            max_length=100,
            verbose_name="Yaradıcı Mətn",
            blank=True,
            default="STORM"
        ),
        slide_text=models.CharField(
            max_length=100,
            verbose_name="Slider Mətni",
            blank=True,
            default=""
        )
    )
    creation_url = models.URLField(
        verbose_name="Yaradıcı Link",
        blank=True,
        default="https://vrproduction.az/"
    )

    class Meta:
        verbose_name = "Footer Məlumatı"
        verbose_name_plural = "Footer Məlumatları"

    def __str__(self):
        return f"Footer Info: {self.safe_translation_getter('description_text', any_language=True)[:30]}..."


class Preloader(TranslatableModel):
    translations = TranslatedFields(
        display_text=models.CharField(
            max_length=200,
            verbose_name="Yüklənir Mətn",
            blank=True,
            default="Dr. Kamil Cəfərov | Yüklənir"
        )
    )
    image = models.ImageField(
        upload_to='preloader/',
        verbose_name="Preloader Şəkli",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Preloader"
        verbose_name_plural = "Preloader"

    def __str__(self):
        return f"Preloader: {self.safe_translation_getter('display_text', any_language=True)[:30]}"


class Sidebar(TranslatableModel):
    translations = TranslatedFields(
        sidebar_text=models.CharField(
            verbose_name="Sidebar Mətn",
            blank=True,
            default=""
        )
    )

    class Meta:
        verbose_name = "Sidebar"
        verbose_name_plural = "Sidebar"
