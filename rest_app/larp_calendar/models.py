from django.db import models

from larp_calendar.settings import UPLOAD_DIR


class Larp(models.Model):
    name = models.CharField(max_length=50)
    organizer = models.CharField(max_length=50)
    website = models.URLField(null=True, blank=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    image = models.ImageField(upload_to=UPLOAD_DIR, null=True, blank=True)
    description = models.TextField()
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.name
