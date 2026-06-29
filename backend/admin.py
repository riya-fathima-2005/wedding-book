from django.contrib import admin
from .models import Venue
from .models import Booking
from .models import Module,Child
from .models import Payment
from .models import VenueMap


admin.site.register(Booking)
admin.site.register(Venue)
admin.site.register(Module)
admin.site.register(Child)
admin.site.register(Payment)
admin.site.register(VenueMap)
