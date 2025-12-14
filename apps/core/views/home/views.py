from django.shortcuts import render
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'pages/home/home.html')


def section3_detail(request, slug):
    section3 = get_object_or_404(Section3, slug=slug)
    section3_details = Section3Detail.objects.filter(section3=section3)
    for detail in section3_details:
        detail.tag_list = [t.strip() for t in detail.tags.split(',')] if detail.tags else []

    context = {
        
        'section3': section3,
        'section3_details': section3_details,
    }
    return render(request, 'pages/home/section3_detail.html', context)
