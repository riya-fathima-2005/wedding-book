from django.urls import path
from .views import VenueMapAPIView

urlpatterns = [
    path("venue-map/", VenueMapAPIView.as_view(), name="venue-map"),
]