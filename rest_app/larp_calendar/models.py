from django.db import models

class Larp(models.Model):
    name = models.CharField(max_length=50)
    organizer = models.CharField(max_length=50)
    website = models.URLField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    image = models.ImageField()
    description = models.TextField()