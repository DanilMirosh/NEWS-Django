from django.contrib import admin

from news.models import News, Place, WeatherSummary

admin.site.register(News)
admin.site.register(Place)
admin.site.register(WeatherSummary)
