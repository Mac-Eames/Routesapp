# from django.db import models
# from django.contrib.gis.db import models
# # Create your models here.

# class Routes(models.Model):
#     name = models.CharField(max_length=100)
#     geometry = models.LineStringField()
#     highway = models.CharField(max_length=100, default='unknown')
    


#     def __str__(self):
#         return self.name

from django.db import models
from django.contrib.gis.db import models as geomodels

class Routes(models.Model):
    name = models.CharField(max_length=100)
    geometry = geomodels.LineStringField()
    highway = models.CharField(max_length=100, default='unknown')
    # path = models.CharField(max_length=255, blank=True, null=True)  # If you need this field

     
    def __str__(self):
      return self.name


    class Meta:
        db_table = 'cleaned_london_road'  # Ensure this matches your database table
