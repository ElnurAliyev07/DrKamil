from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from apps.blog.models import Blog, BlogItem   # öz app adını yaz

def blog(request):
    # Bütün BlogItem-ləri gətiririk və 4-lük səhifələyirik
    items = BlogItem.objects.all().order_by('-id')
    paginator = Paginator(items, 4)  # 1 səhifədə 4 item
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    for item in page_obj:
        item.tag_list = [t.strip() for t in item.tags.split(',')] if item.tags else []
    
    context = {

        'blogs': Blog.objects.all(),
        'page_obj': page_obj,      # ✅ pagination üçün
    }
    return render(request, 'pages/blog/blog.html', context)


def blog_detail(request, slug):
    # Slug vasitəsilə bir item tapırıq
    item = get_object_or_404(BlogItem, slug=slug)
    detail = getattr(item, 'detail', None)  # BlogDetail varsa çək

    prev_item = BlogItem.objects.filter(id__lt=item.id).order_by('-id').first()
    next_item = BlogItem.objects.filter(id__gt=item.id).order_by('id').first()
    tag_list = [t.strip() for t in item.tags.split(',')] if item.tags else []

    blog_seo = getattr(detail, 'seo', None) if detail else None

    if blog_seo:
        if blog_seo.og_image:
            blog_seo.og_image = request.build_absolute_uri(blog_seo.og_image.url)

        if blog_seo.twitter_image:
            blog_seo.twitter_image = request.build_absolute_uri(blog_seo.twitter_image.url)

    context = {
        'item': item,
        'detail': detail,
        'prev_item': prev_item,
        'next_item': next_item,
        'tag_list': tag_list,

        'blog_seo': blog_seo,
    }
    return render(request, 'pages/blog/blog_detail.html', context)
