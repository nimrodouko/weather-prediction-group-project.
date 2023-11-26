from django.db import models


class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind = models.FloatField()
    soil = models.IntegerField(choices=[(0, 'Clay'), (1, 'Loam'), (2, 'Sand'), (3, 'Silt')])
    terrain = models.IntegerField(choices=[(0, 'Lowland'), (1, 'Highland')])


# Create your models here.
