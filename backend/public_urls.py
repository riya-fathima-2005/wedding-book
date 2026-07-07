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
    path(
    "api/weddings/<int:pk>/",
    views.WeddingDetailView.as_view(),
    name="wedding-detail"
),

    path(
    "create-payment/",
    views.create_payment,
    name="create_payment"
),

path(
    "save-payment/",
    views.save_payment,
    name="save_payment"
),
path(
    "has-paid/<int:wedding_id>/",
    views.has_paid,
    name="has_paid"
),
    path("api/blogs/", views.blog_api, name="blog_api"),
    path("api/blogs/<slug:slug>/", views.single_blog_api, name="single_blog_api"),

path("pages/", views.pages, name="pages"),
path("add-page/", views.add_page, name="add_page"),
path("edit-page/<int:id>/", views.edit_page, name="edit_page"),
path("delete-page/<int:id>/", views.delete_page, name="delete_page"),
path(
    "api/pages/",
    views.pages_api,
    name="pages_api"
),
path(
    "api/pages/<slug:slug>/",
    views.single_page_api,
    name="single_page_api",
),

]