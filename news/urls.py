from django.urls import path

from news.views import NewsViewSet

app_name = 'news'

urlpatterns = [
    path('news/', NewsViewSet.as_view({'get': 'list', 'post': 'create'}), name='news'),
]
