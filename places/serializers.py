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
            try:
                lon, lat = map(float, coordinates.split(","))
            except ValueError:
                raise serializers.ValidationError(
                    "You must set geom in format: 'number, number'"
                )
            return Point(lon, lat)
        return None

    def create(self, validated_data):
        validated_data["geom"] = self.get_geom(None)
        return super().create(validated_data)
