from django.core.cache import cache
from django.urls import resolve, Resolver404
from django.utils.translation import get_language
from .models import PageSEO, Sidebar, SocialLink, SiteLogo, ContactInfo, FooterInfo, Preloader
from apps.rinoplastika.models import ServiceItem
from apps.home.models import (
    HeroSection, HeroSectionImages, HeroContent,
    IntroSection,
    Services, Faqs, FaqsItem,
    Comment, CommentItem,
    Blog, BlogItem,
    Appointment,
)

def site_context(request):
    language_code = get_language()
    page_type = 'custom'

    # Default SEO dəyərləri (sabit, modeldən çəkilmir)
    seo_data = {
        'seo_title': 'Dr. Kamil | Rinoplastika və Plastik Cərrahiyyə Mütəxəssisi',
        'seo_description': 'Dr. Kamil — peşəkar rinoplastika və plastik cərrahiyyə xidməti. Burun estetikası, üz və bədən formalaşdırılması üzrə ixtisaslaşmış həkim.',
        'meta_keywords': 'rinoplastika, burun estetikası, plastik cərrahiyyə, dr kamil, estetik əməliyyat, bakı rinoplastika, burun əməliyyatı',
        'og_title': 'Dr. Kamil | Rinoplastika üzrə ixtisaslaşmış həkim',
        'og_description': 'Peşəkar rinoplastika və plastik cərrahiyyə xidməti. Dr. Kamil ilə təbii və estetik nəticələr əldə edin.',
        'og_image': None,
        'logo': None,
        'canonical_url': request.build_absolute_uri(),
        'no_index': False,
        'no_follow': False,
    }

    try:
        match = resolve(request.path_info)
        view_name = match.view_name or ''

        # Sənin URL adlarına əsasən səhifə tipləri
        if view_name in ['home', 'about', 'contact', 'appointment']:
            page_type = view_name

        elif view_name == 'blog':
            page_type = 'blog'
            seo_data.update({
                'seo_title': f"Blog | {seo_data['seo_title']}",
                'seo_description': f"Explore our latest blog posts | {seo_data['seo_description']}",
                'og_title': 'Blog',
                'og_description': 'Explore our latest blog posts',
            })

        elif view_name == 'rhinoplastica':
            page_type = 'services'
            seo = PageSEO.get_seo(page_type='services', language=language_code)
            default_title = f"Services | {seo_data['seo_title']}"
            default_description = f"Explore our professional services | {seo_data['seo_description']}"
            seo_data.update({
                'seo_title': seo.seo_title if seo and seo.seo_title else default_title,
                'seo_description': seo.seo_description if seo and seo.seo_description else default_description,
                'og_title': seo.og_title if seo and seo.og_title else 'Services',
                'og_description': seo.og_description if seo and seo.og_description else default_description,
                'og_image': seo.og_image.url if seo and seo.og_image else None,
                'logo': seo.logo.url if seo and seo.logo else None,
                'canonical_url': seo.canonical_url if seo and seo.canonical_url else request.build_absolute_uri(),
                'no_index': seo.no_index if seo else False,
                'no_follow': seo.no_follow if seo else False,
            })

        # PageSEO modelindən əlavə SEO məlumatları
        seo = PageSEO.get_seo(page_type=page_type, language=language_code)
        if seo:
            seo_data.update({
                'seo_title': seo.seo_title or seo_data['seo_title'],
                'seo_description': seo.seo_description or seo_data['seo_description'],
                'meta_keywords': seo.meta_keywords or seo_data['meta_keywords'],
                'og_title': seo.og_title or seo_data['og_title'],
                'og_description': seo.og_description or seo_data['og_description'],
                'og_image': seo.og_image.url if seo.og_image else seo_data['og_image'],
                'logo': seo.logo.url if seo.logo else seo_data['logo'],
                'canonical_url': seo.canonical_url or seo_data['canonical_url'],
                'no_index': seo.no_index,
                'no_follow': seo.no_follow,
            })

    except Resolver404:
        pass

    # Absolute og_image URL yarat
    if seo_data['og_image']:
        seo_data['og_image'] = request.build_absolute_uri(seo_data['og_image'])

    return {
        'seo_data': seo_data,
        'page_type': page_type,
    }


def global_context(request):
    # Hero bölməsi
    hero_section = HeroSection.objects.first()
    hero_images = hero_section.images.all() if hero_section else []
    hero_contents = HeroContent.objects.all()

    # Intro bölməsi
    intro = IntroSection.objects.first()

    # Services bölməsi
    services = Services.objects.first()
    service_items = services.items.all()[:4] if services else []

    # Faqs
    faqs = Faqs.objects.first()
    faqs_items = faqs.items.all() if faqs else []

    # Comments / Testimonials
    comments = Comment.objects.first()
    comment_items = comments.items.all() if comments else []

    # Blog
    blog = Blog.objects.first()
    blog_items = blog.items.all()[:4] if blog else []

    # Appointment
    appointment = Appointment.objects.first()

    # Sabit məlumatlar
    social_links = SocialLink.objects.all()
    logo = SiteLogo.objects.first()
    contact = ContactInfo.objects.first()
    footer = FooterInfo.objects.first()
    preloader = Preloader.objects.first()
    sidebar = Sidebar.objects.first()

    return {
        'hero_section': hero_section,
        'hero_images': hero_images,
        'hero_contents': hero_contents,
        'intro': intro,
        'services': services,
        'service_items': service_items,
        'faqs': faqs,
        'faqs_items': faqs_items,
        'comments': comments,
        'comment_items': comment_items,
        'blog': blog,
        'blog_items': blog_items,
        'appointment': appointment,
        'social_links': social_links,
        'logo': logo,
        'contact': contact,
        'footer': footer,
        'preloader': preloader,
        'sidebar': sidebar,
    }
