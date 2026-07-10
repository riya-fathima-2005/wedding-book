from rest_framework import serializers
from .models import Venue, Booking, Wedding, WeddingCard


from .models import VenueMap

class VenueMapSerializer(serializers.ModelSerializer):
    venue_name = serializers.CharField(source="venue.name")
    location = serializers.CharField(source="venue.location")

    class Meta:
        model = VenueMap
        fields = [
            "id",
            "venue_name",
            "location",
            "latitude",
            "longitude"
        ]
        

class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = "__all__"
        read_only_fields = ["user"]

class VenueSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Venue
        fields = "__all__"

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

class BookingSerializer(serializers.ModelSerializer):

    venue_name = serializers.CharField(
        source='venue.name',
        read_only=True
    )

    class Meta:
        model = Booking
        fields = '__all__'


class WeddingCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingCard
        fields = "__all__"
        