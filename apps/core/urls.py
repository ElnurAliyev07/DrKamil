from django.urls import path
from .views.home.views import home, section3_detail
from .views.about.views import about, articles, presentations, whythisdr
from .views.rinoplastika.views import rhino, about_rino, rhinoplastica, rhinoplastica_detail
from .views.blog.views import blog, blog_detail
from .views.contact.views import contact, appointment

urlpatterns = [
    path('', home, name='home'),  # Ana səhifə
    path('home/<slug:slug>/', section3_detail, name='section3_detail'),

    path('about/', about, name='about'),  # Haqqımda
    path('about/articles/', articles, name='articles'),  # Məqalələr
    path('about/presentations/', presentations, name='presentations'),  # Təqdimatlar

    path('contact/', contact, name='contact'),  # Haqqımda
    path('appointment/', appointment, name='appointment'),  # Haqqımda

    path('why-dr-kamil-jafarov/', whythisdr, name='whythisdr'),  # Niyə Dos. Dr. Cavid Cabbarzadə?

    path('threatment-innovation/', rhino, name='rhino'),  # Rinoplastika ilə bağlı yeniliklər
    path('about-rhinoplastica/', about_rino, name='about_rino'),  # Rinoplastika ilə bağlı yeniliklər

    path('services/', rhinoplastica, name='rhinoplastica'),  # Rinoplastika
    path('services/<slug:slug>/', rhinoplastica_detail, name='rhinoplastica_detail'),  # Rinoplastika detail

    path('blog/', blog, name='blog'),  # Blog
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),  # Blog detail
    
]
