from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.TextField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    LocationType = models.TextChoices(
        'LocationType', 'Hawaii Kauai Lanai Maui Molokai Oahu')
    location = models.CharField(choices=LocationType.choices, max_length=10)
