from django.db import models

# Create your models here.

class Marker(models.Model):
    nome = models.CharField(max_length = 50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    cor = models.CharField(max_length = 10)
    icone = models.CharField(max_length = 50)