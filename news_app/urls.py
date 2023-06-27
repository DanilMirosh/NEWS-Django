from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django_summernote import urls as summernote_urls
from rest_framework.routers import DefaultRouter

from news.views import NewsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('summernote/', include(summernote_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
