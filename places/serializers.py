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

    def get_geom(self, obj) -> Point | None:
        """
        Get the Point geometry based on the provided coordinates.
        Args:
            obj: The object for which to get the Point geometry.
        Returns:
            Point | None: The Point geometry if coordinates are provided, otherwise None.
        Raises:
            serializers.ValidationError: If the coordinates are not in the correct format.
        """

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

    def create(self, validated_data: dict) -> Place:
        """
        Create a new Place instance.
        Args:
            validated_data (dict): The validated data for creating the Place instance.
        Returns:
            Place: The created Place instance.
        """
        validated_data["geom"] = self.get_geom(None)
        return super().create(validated_data)

    def update(self, instance: Place, validated_data: dict) -> Place:
        """
        Update an existing Place instance.
        Args:
            instance (Place): The existing Place instance to update.
            validated_data (dict): The validated data for updating the Place instance.
        Returns:
            Place: The updated Place instance.
        """
        validated_data["geom"] = self.get_geom(None)
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.geom = validated_data.get("geom", instance.geom)
        instance.save()
        return instance
