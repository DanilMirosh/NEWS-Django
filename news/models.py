from django.contrib.gis.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='new_images')
    preview_image = models.ImageField(upload_to='new_images/previews')
    text = models.TextField()
    publication_date = models.DateField()
    author = models.CharField(max_length=100)


class Place(models.Model):
    name = models.CharField(max_length=200)
    coordinates = models.PointField()
    rating = models.IntegerField()


class WeatherSummary(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    pressure = models.DecimalField(max_digits=5, decimal_places=2)
    wind_direction = models.CharField(max_length=50)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
