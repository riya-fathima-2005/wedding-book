"""
URL configuration for myproject project.
"""

from backend import views
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# JWT IMPORTS
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('django-admin/', admin.site.urls),

    path("admin/", views.index, name="dashboard"),

    # APP URLS
    path('', include('backend.urls')),
    # JWT URLS
    path('api/token/', TokenObtainPairView.as_view()),

    path('api/token/refresh/', TokenRefreshView.as_view()),
    
    path("ckeditor5/", include('django_ckeditor_5.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)