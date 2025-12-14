from django.shortcuts import render
from apps.rinoplastika.models import Innovation, Service, ServiceItem, AboutRino
from django.shortcuts import get_object_or_404

def rhino(request):
    context = {

        'innovation': Innovation.objects.first(),
    }
    return render(request, 'pages/rinoplastika/rhino.html', context)

def about_rino(request):
    context = {

        'about_rino': AboutRino.objects.first(),
    }
    return render(request, 'pages/rinoplastika/about_rino.html', context)
    

def rhinoplastica(request):
    context = {

        'services': Service.objects.all(),
    }
    return render(request, 'pages/rinoplastika/rinoplastika.html', context)

def rhinoplastica_detail(request, slug):
    item = get_object_or_404(ServiceItem, slug=slug)
    service = item.service
    detail = getattr(item, 'detail', None)  # ServiceDetail obyekti
    seo = getattr(detail, 'seo', None) if detail else None  # ServiceDetailSeo obyekti

    if seo:
        if seo.og_image:
            seo.og_image = request.build_absolute_uri(seo.og_image.url)

        if seo.twitter_image:
            seo.twitter_image = request.build_absolute_uri(seo.twitter_image.url)

    context = {

        'service': service,
        'item': item,
        'detail': detail,
        'seo': seo,   # ✅ SEO məlumatlarını template-ə ötürürük
    }
    return render(request, 'pages/rinoplastika/rinoplastika_detail.html', context)