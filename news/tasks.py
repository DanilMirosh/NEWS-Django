from random import randint

from celery import shared_task

from news.models import Place, WeatherSummary


@shared_task
def send_news_mail():
    # Ваш код для отправки email
    pass


@shared_task
def fetch_weather_summary(place_id):
    place = Place.objects.get(id=place_id)
    # Ваш код для получения сводки погоды
    temperature = randint(-20, 40)
    humidity = randint(0, 100)
    pressure = randint(700, 800)
    wind_direction = randint(0, 360)
    wind_speed = randint(0, 10)

    # Создайте новую сводку погоды и сохраните ее в базе данных
    weather_summary = WeatherSummary(place=place, temperature=temperature, humidity=humidity,
                                     pressure=pressure, wind_direction=wind_direction, wind_speed=wind_speed)
    weather_summary.save()
