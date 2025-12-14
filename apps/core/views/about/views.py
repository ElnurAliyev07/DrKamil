
from django.shortcuts import render
from apps.about.models import About, Article, Presentation, WhyThisDr

def about(request):
    about_instance = About.objects.first()

    context = {
        'about': about_instance, 
    }

    return render(request, 'pages/about/about.html', context)

def articles(request):
    context = {
        'articles': Article.objects.first(),
    }
    return render(request, 'pages/about/articles.html', context)

def presentations(request):
    presentation = Presentation.objects.prefetch_related('items').first()
    items = presentation.items.all() if presentation else []

    # İtemləri iki sütuna bölürük
    mid = (len(items) + 1) // 2
    col1 = items[:mid]
    col2 = items[mid:]

    context = {
        'presentation': presentation,
        'col1': col1,
        'col2': col2,
    }
    return render(request, 'pages/about/presentations.html', context)



def whythisdr(request):
    context = {
        'whythisdr': WhyThisDr.objects.first(),
    }
    return render(request, 'pages/home/whythisdr.html', context)