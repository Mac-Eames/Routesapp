from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Routes(models.Model):
    name = models.CharField(max_length=100)
    path = models.LineStringField()


    def __str__(self):
        return self.name