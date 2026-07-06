from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
import uuid



        # PROFILE MODEL

class Profile(models.Model):

            ROLE_CHOICES = (

                ('admin', 'Admin'),

                ('host', 'Host'),

                ('user', 'User'),

            )

            user = models.OneToOneField(
                User,
                on_delete=models.CASCADE
            )

            image = models.ImageField(
                upload_to='profiles/',
                default='default.png',
                null=True,
                blank=True
            )

            phone = models.CharField(
                max_length=20,
                blank=True,
                null=True
            )

            address = models.TextField(
                blank=True,
                null=True
            )

            bio = models.TextField(
                blank=True,
                null=True
            )

            role = models.CharField(
                max_length=20,
                choices=ROLE_CHOICES,
                default='user'
            )

            created_at = models.DateTimeField(
            null=True,
            blank=True
        )

            def __str__(self):

                return self.user.username


        # VENUE MODEL
class Venue(models.Model):

            name = models.CharField(max_length=100)

            location = models.CharField(max_length=100)

            bride_name = models.CharField(
                max_length=100,
                blank=True,
                null=True
            )

            groom_name = models.CharField(
                max_length=100,
                blank=True,
                null=True
            )

            status = models.CharField(
            max_length=20,
            choices=[
                ('Available', 'Available'),
                ('Booked', 'Booked')
            ],
            default='Available'
        )
            
            price = models.IntegerField()

            image = models.ImageField(
                upload_to='venues/',
                null=True,
                blank=True
            )

            description = models.TextField(
                null=True,
                blank=True
            )


        # BOOKING MODEL



class Booking(models.Model):

            # Logged-in User

            # which user which venue boocked

            user = models.ForeignKey(
                User,
                on_delete=models.CASCADE,
                related_name='bookings',
                null=True,
                blank=True
            )

            customer_name = models.CharField(
                max_length=100
            )

            customer_email = models.EmailField()

            customer_phone = models.CharField(
                max_length=15
            )

            venue = models.ForeignKey(
                Venue,
                on_delete=models.CASCADE
            )
            

            booking_date = models.DateField()

            guests = models.IntegerField()

            total_amount = models.IntegerField()

            status = models.CharField(
                max_length=50,
                choices=[
                    ('Pending', 'Pending'),
                    ('Confirmed', 'Confirmed'),
                    ('Cancelled', 'Cancelled')
                ],
                default='Pending'
            )

            created_at = models.DateTimeField(
                auto_now_add=True
            )

            def __str__(self):

                return f"{self.customer_name} - {self.venue.name}"


        # MODULE MODEL

class Module(models.Model):

            name = models.CharField(
                max_length=100
            )

            url_name = models.CharField(
                max_length=50,
                blank=True,
                null=True
            )

            icon = models.CharField(
                max_length=50,
                blank=True
            )

            def __str__(self):

                return self.name


        # CHILD MODEL

class Child(models.Model):

            module = models.ForeignKey(
                Module,
                on_delete=models.CASCADE,
                related_name="children"
            )

            name = models.CharField(
                max_length=100
            )

            url_name = models.CharField(
                max_length=50,
                blank=True,
                null=True
            )

            def __str__(self):

                return self.name


        # USER GROUP MODEL

class UserGroup(models.Model):

            STATUS_CHOICES = (
                ('Active', 'Active'),
                ('Inactive', 'Inactive'),
            )

            name = models.CharField(
                max_length=100
            )

            description = models.TextField()

            status = models.CharField(
                max_length=20,
                choices=STATUS_CHOICES
            )

            def __str__(self):

                return self.name

class Permission(models.Model):
    group_name = models.CharField(max_length=100)

    add_users = models.BooleanField(default=False)
    edit_users = models.BooleanField(default=False)
    delete_users = models.BooleanField(default=False)
    manage_bookings = models.BooleanField(default=False)
    manage_venues = models.BooleanField(default=False)

    def __str__(self):
            return self.group_name

class Payment(models.Model):

    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    wedding = models.ForeignKey(
    "Wedding",
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    payer_name = models.CharField(max_length=100)

    venue_name = models.CharField(max_length=200)

    razorpay_order_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    razorpay_payment_id = models.CharField(
        max_length=255,
        unique=True
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_status = models.CharField(
        max_length=20,
        default="Success"
    )

    payment_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.razorpay_payment_id



class Wedding(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(max_length=50)

    firstname = models.CharField(max_length=100)

    lastname = models.CharField(max_length=100)

    partner_firstname = models.CharField(max_length=100)

    partner_lastname = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(
    upload_to="weddings/",
    blank=True,
    null=True
)
    invitation = models.FileField(
    upload_to="wedding_invitations/",
    blank=True,
    null=True
)
    

    youtube_link = models.URLField(
        blank=True,
        null=True
    )

    wedding_date = models.DateField()

    wedding_time = models.TimeField()

    venue = models.ForeignKey(
        Venue,
        on_delete=models.SET_NULL,
        null=True
    )

    food_type = models.CharField(max_length=50)

    alcohol_served = models.CharField(max_length=20)

    language = models.CharField(max_length=50)

    dress_code = models.CharField(max_length=100)

    description = models.TextField()
    
    custom_venue = models.CharField(
    max_length=255,
    blank=True,
    null=True
)

    venue_price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    blank=True,
    null=True
)
    manager_phone = models.CharField(
    max_length=15,
    blank=True,
    null=True
)

    latitude = models.FloatField(
    blank=True,
    null=True
)

    longitude = models.FloatField(
    blank=True,
    null=True
)

    payment_status = models.CharField(
        max_length=20,
        default="Pending"

        
    )
    venue_map_link = models.URLField(blank=True, null=True)
    

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.firstname} & {self.partner_firstname}"
    
class VenueMap(models.Model):

    venue_name = models.CharField(max_length=200)

    latitude = models.FloatField(
        null=True,
        blank=True
    )
    
    longitude = models.FloatField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.venue_name
    
class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




class Blog(models.Model):

    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        related_name="blogs",
        null=True,
        blank=True
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    image = models.ImageField(upload_to="blogs/")
    short_description = models.TextField(blank=True, default="")

    content = CKEditor5Field("Text", config_name="extends")

    author = models.CharField(max_length=100, default="Admin")

    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=300, blank=True)

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(self.title)
            unique_slug = base_slug

            while Blog.objects.filter(
                slug=unique_slug
            ).exists():

                unique_slug = f"{base_slug}-{uuid.uuid4().hex[:4]}"

            self.slug = unique_slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title