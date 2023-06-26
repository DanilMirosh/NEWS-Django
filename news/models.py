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
