from django.urls import path, include
from rest_framework import routers

from places.views import PlaceListView

router = routers.DefaultRouter()
router.register("", PlaceListView)
urlpatterns = [
    path("", include(router.urls)),
]

app_name = "places"
