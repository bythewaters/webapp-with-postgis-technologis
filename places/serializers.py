from django.contrib.gis.geos import Point
from rest_framework import serializers

from places.models import Place


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
            "id",
            "name",
            "description",
            "geom",
        ]

    def get_geom(self, obj):
        coordinates = self.context["request"].data.get("geom")
        if coordinates:
            lon, lat = map(float, coordinates.split(","))
            return Point(lon, lat)
        return None

    def create(self, validated_data):
        validated_data["geom"] = self.get_geom(None)
        return super().create(validated_data)
