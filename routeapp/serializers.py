from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Routes

class RouteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Routes
        geo_field = 'geometry'
        fields = ('name', 'highway')