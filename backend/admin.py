from django.contrib import admin
from .models import Venue, Booking, Module, Child, Payment, VenueMap, Blog, BlogCategory


admin.site.register(Booking)
admin.site.register(Venue)
admin.site.register(Module)
admin.site.register(Child)
admin.site.register(Payment)
admin.site.register(VenueMap)
admin.site.register(BlogCategory)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_published", "created_at")
    