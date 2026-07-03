from django.urls import path
from . import views
from .views import ProfileAPIView, ChangePasswordAPIView, WeddingListCreateView

urlpatterns = [

    path('', views.index, name='index'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),

    # API
    path('api/venues/', views.venue_api),
    path('api/bookings/', views.booking_api),
    path("api/contact/", views.contact_test),

    path('api/my-bookings/', views.my_bookings_api),
    path('api/cancel-booking/<int:booking_id>/', views.cancel_booking),

    path('api/profile/', ProfileAPIView.as_view(), name='profile-api'),
    path('api/change-password/', ChangePasswordAPIView.as_view(), name='change-password'),

    path('api/weddings/', WeddingListCreateView.as_view(), name='weddings'),

    path("api/blogs/", views.blog_api, name="blog_api"),
    path("api/blogs/<slug:slug>/", views.single_blog_api, name="single_blog_api"),
]