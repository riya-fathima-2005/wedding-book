from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='dashboard'),

    path('venues/', views.venues, name='venues'),
    path('add-venue/', views.add_venue, name='add_venue'),
    path('edit-venue/<int:id>/', views.edit_venue, name='edit_venue'),
    path('delete-venue/<int:id>/', views.delete_venue, name='delete_venue'),

    path('bookings/', views.bookings, name='bookings'),
    path('view_booking/<int:id>/', views.view_booking, name='view_booking'),
    path('edit_booking/<int:id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:id>/', views.delete_booking, name='delete_booking'),

    path('allusers/', views.allusers, name='allusers'),
    path('add_user/', views.add_user, name='add_user'),
    path('edit-user/<int:id>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),

    path('payment/', views.payment_list, name='payment'),

    path('venue-map/', views.venue_map, name='venue_map'),

    path("blog/", views.blog, name="blog"),
    path("blog-list/", views.blog_list, name="blog_list"),
    path("edit-blog/<int:id>/", views.edit_blog, name="edit_blog"),
    path("delete-blog/<int:id>/", views.delete_blog, name="delete_blog"),
    path('profile/', views.profile_page, name='profile'),
path('edit-profile/', views.edit_profile, name='edit_profile'),

path("add-category/", views.add_category, name="add_category"),


# THIS ONE MISSING
path('save_permission/<int:group_id>/', views.save_permission, name='save_permission'),
path("save-payment/", views.save_payment),

# All User Groups
path('allusergroups/', views.allusergroups, name='allusergroups'),
path('create-groups/', views.create_groups, name='create_groups'),
path('add_allusergroups/', views.add_allusergroups, name='add_allusergroups'),
path('edit_allusergroups/<int:id>/', views.edit_allusergroups, name='edit_allusergroups'),
path('delete-group/<int:id>/', views.delete_group, name='delete_group'),
path( "has-paid/<int:wedding_id>/", views.has_paid,name="has_paid"),
path("create-payment/", views.create_payment),


path(
    "wedding-cards/",
    views.wedding_cards,
    name="wedding_cards"
),

path(
    "add-wedding-card/",
    views.add_wedding_card,
    name="add_wedding_card"
),

path(
    "edit-wedding-card/<int:id>/",
    views.edit_wedding_card,
    name="edit_wedding_card"
),

path(
    "delete-wedding-card/<int:id>/",
    views.delete_wedding_card,
    name="delete_wedding_card"
),
path(
    "add-wedding-card/",
    views.add_wedding_card,
    name="add_wedding_card"
),






path(
    "weddings/",
    views.wedding_list,
    name="wedding_list"
),

path(
    "add-wedding/",
    views.add_wedding,
    name="add_wedding"
),

path(
    "edit-wedding/<int:id>/",
    views.edit_wedding,
    name="edit_wedding"
),

path(
    "delete-wedding/<int:id>/",
    views.delete_wedding,
    name="delete_wedding"
),


]