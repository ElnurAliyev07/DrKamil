from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns  # <- çoxdillilik üçün

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # dil dəyişimi üçün URL
]

urlpatterns += i18n_patterns(
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    path("", include("apps.core.urls")),
    prefix_default_language=False,  # <<< burası əsas məsələ
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
