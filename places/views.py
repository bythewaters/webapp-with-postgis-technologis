from rest_framework import viewsets

from places.models import Place
from places.serializers import PlaceListSerializer


class PlaceListView(viewsets.ModelViewSet):
    serializer_class = PlaceListSerializer
    queryset = Place.objects.all()

