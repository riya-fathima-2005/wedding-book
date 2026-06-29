"""
URL configuration for myproject project.
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# JWT IMPORTS
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('django-admin/', admin.site.urls),

    # APP URLS
    path('', include('backend.urls')),
    # JWT URLS
    path('api/token/', TokenObtainPairView.as_view()),

    path('api/token/refresh/', TokenRefreshView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)