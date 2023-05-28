from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance as DistanceFunc
from django.db.models import QuerySet
from rest_framework import viewsets

from places.models import Place
from places.serializers import PlaceListSerializer


class PlaceListView(viewsets.ModelViewSet):
    serializer_class = PlaceListSerializer
    queryset = Place.objects.all()

    def get_queryset(self) -> QuerySet[Place]:
        queryset = self.queryset
        latitude = self.request.query_params.get("lat", None)
        longitude = self.request.query_params.get("lon", None)
        num_points = int(self.request.query_params.get("num_points", 1))
        if latitude and longitude:
            point = Point(float(longitude), float(latitude), srid=4326)
            return queryset.annotate(
                distance=DistanceFunc("geom", point)
            ).order_by(
                "distance"
            )[:num_points]
        return queryset

