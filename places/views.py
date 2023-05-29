from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance as DistanceFunc
from django.db.models import QuerySet
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from places.models import Place
from places.serializers import PlaceListSerializer


class PlaceListView(viewsets.ModelViewSet):
    serializer_class = PlaceListSerializer
    queryset = Place.objects.all()

    def get_queryset(self) -> QuerySet[Place]:
        """
        Get the queryset of places with optional coordinate parameter
        Args:
            self: The instance of the view.
        Returns:
            QuerySet[Place]: The filtered queryset of places.
        Raises:
            ValidationError: If the coordinate is not provided in the correct format.
        """
        queryset = self.queryset
        coordinate = self.request.query_params.get("coordinate", None)
        if coordinate:
            try:
                lon, lat = map(float, coordinate.split(","))
                point = Point(float(lon), float(lat), srid=4326)
            except ValueError:
                raise ValidationError("You must set geom in format: 'number,number'")
            return queryset.annotate(
                distance=DistanceFunc("geom", point)
            ).order_by(
                "distance"
            )[:1]
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "coordinate",
                type=OpenApiTypes.STR,
                description="finding the nearest place to "
                            "the entered coordinates "
                            "ex.(?coordinate=56.3443,30.4343)",
            )]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
