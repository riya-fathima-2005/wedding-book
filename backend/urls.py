from django.urls import path
from . import views

from .views import ProfileAPIView, ChangePasswordAPIView, WeddingListCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# JWT TOKEN

urlpatterns = [

    path(
    'api/token/',
    TokenObtainPairView.as_view(),
    name='token_obtain_pair'
),

path(
    'api/token/refresh/',
    TokenRefreshView.as_view(),
    name='token_refresh'
),



    path('', views.index, name='index'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),

    # Venue
    path('venue/<int:id>/', views.venue_detail, name='venue_detail'),
    path('venues/', views.venues, name='venues'),
    path('edit-venue/<int:id>/', views.edit_venue, name='edit_venue'),
    path('delete-venue/<int:id>/', views.delete_venue, name='delete_venue'),
    path('add-venue/', views.add_venue, name='add_venue'),

    # API
    path('api/venues/', views.venue_api),
    path('api/bookings/', views.booking_api),
    path('api/venue-map/', views.VenueMapAPIView.as_view()),

    # Booking
    path('bookings/', views.bookings, name='bookings'),
    path('view_booking/<int:id>/', views.view_booking, name='view_booking'),
    path('edit_booking/<int:id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:id>/', views.delete_booking, name='delete_booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('create-booking/<int:venue_id>/', views.create_booking, name='create_booking'),
    path('api/my-bookings/', views.my_bookings_api, name='my_bookings_api'),
    path('api/cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

    # All User
    path('allusers/', views.allusers, name='allusers'),
    path('add_user/', views.add_user, name='add_user'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),
    path('edit-user/<int:id>/', views.edit_user, name='edit_user'),
    path('save_permission/<int:group_id>/', views.save_permission, name='save_permission'),
    path("api/contact/", views.contact_test),

    # All User Group
    path('allusergroups/', views.allusergroups, name='allusergroups'),
    path('create-groups/', views.create_groups, name='create_groups'),
    path('add_allusergroups/', views.add_allusergroups, name='add_allusergroups'),
    path('edit_allusergroups/<int:id>/', views.edit_allusergroups, name='edit_allusergroups'),
    path('delete-group/<int:id>/', views.delete_group, name='delete_group'),

    # Profile
    path('profile/', views.profile_page, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('api/profile/', ProfileAPIView.as_view(), name='profile-api'),
    path('api/change-password/', ChangePasswordAPIView.as_view(), name='change-password'),

    # Payment
    path('create-payment/', views.create_payment, name='create_payment'),
    path('payment/', views.payment_list, name='payment'),
    path('save-payment/', views.save_payment, name='save_payment'),
    path('api/weddings/', WeddingListCreateView.as_view(), name='weddings'),

    # Venue Map Dashboard
    path('venue-map/', views.venue_map, name='venue_map'),

    # BLOG
    path("blog/", views.blog, name="blog"),
    path("blog-list/", views.blog_list, name="blog_list"),
    path("edit-blog/<int:id>/", views.edit_blog, name="edit_blog"),
    path("delete-blog/<int:id>/", views.delete_blog, name="delete_blog"),   
   path("api/blogs/", views.blog_api, name="blog_api"),
   path("api/blogs/<slug:slug>/", views.single_blog_api, name="single_blog_api"),




]
