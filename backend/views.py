from urllib import request
from .models import Page, Payment
from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import RefreshToken

from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from rest_framework.permissions import AllowAny
from .models import VenueMap
from .serializers import VenueMapSerializer
from django.db.models import Sum
from .models import Blog, BlogCategory
from .forms import BlogForm, PageForm

from .models import BlogCategory
from django.utils.text import slugify

import razorpay
from django.http import JsonResponse
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Venue
from .models import Booking
from .models import UserGroup

from .serializers import VenueSerializer
from .serializers import BookingSerializer
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import check_password
from django.db.models import Q

from django.contrib.auth import ( authenticate, login, logout)

from django.contrib import messages
from .models import Permission
import traceback


from .models import Payment
from django.http import HttpResponse, JsonResponse
from .models import Wedding
from .serializers import WeddingSerializer
from rest_framework import generics

# REST FRAMEWORK
from rest_framework.decorators import ( api_view, permission_classes )
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import ( IsAuthenticated )
from rest_framework_simplejwt.tokens import (RefreshToken)

from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response

        


# index
from django.db.models import Sum

def index(request):

    # total users
    users_count = User.objects.count()

    # total bookings
    bookings_count = Booking.objects.count()

    # revenue sum
    total_revenue = Booking.objects.aggregate(
        total=Sum("total_amount")
    )["total"] or 0

    # latest 5 bookings
    recent_bookings = Booking.objects.order_by(
        "-id"
    )[:5]

    # search
    query = request.GET.get("q")
    venues = None

    if query:
        venues = Venue.objects.filter(
            name__icontains=query
        )

    context = {
        "users_count": users_count,
        "bookings_count": bookings_count,
        "total_revenue": total_revenue,
        "recent_bookings": recent_bookings,
        "query": query,
        "venues": venues,
    }

    return render(
        request,
        "index.html",
        context
    )


@api_view(["POST"])
def contact_test(request):

    print("===== CONTACT API HIT =====")
    print(request.data)

    fullname = request.data.get("fullname")
    email = request.data.get("email")
    phone = request.data.get("phone")
    message = request.data.get("message")

    print(fullname, email, phone)

    try:
        send_mail(
            subject=f"Wedding Contact from {fullname}",
            message=f"""
Name: {fullname}
Email: {email}
Phone: {phone}

Message:
{message}
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        print("EMAIL SENT SUCCESSFULLY")

        return Response(
            {"message": "Message Sent Successfully"},
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        print("EMAIL ERROR:", str(e))
        traceback.print_exc()

        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    # ================= AUTHENTICATION =================


def login_view(request):

        if request.method == 'POST':

            username = request.POST.get(
                'username'
            )

            password = request.POST.get(
                'password'
            )

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect('index')

            else:

                messages.error(
                    request,
                    'Invalid Username Or Password'
                )

        return render(request, 'login.html')


def register(request):

        if request.method == 'POST':

            username = request.POST.get(
                'username'
            )

            email = request.POST.get(
                'email'
            )

            first_name = request.POST.get(
                'first_name'
            )

            last_name = request.POST.get(
                'last_name'
            )

            password = request.POST.get(
                'password'
            )

            confirm_password = request.POST.get(
                'confirm_password'
            )

            # PASSWORD CHECK
            if password != confirm_password:

                messages.error(
                    request,
                    'Passwords Do Not Match'
                )

                return redirect('register')

            # USERNAME EXISTS
            if User.objects.filter(
                username=username
            ).exists():

                messages.error(
                    request,
                    'Username Already Exists'
                )

                return redirect('register')

            # EMAIL EXISTS
            if User.objects.filter(
                email=email
            ).exists():

                messages.error(
                    request,
                    'Email Already Exists'
                )

                return redirect('register')

            # CREATE USER
            User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )

            messages.success(
                request,
                'Registration Successful'
            )

            return redirect('login')

        return render(
            request,
            'register.html'
        )


def logout_view(request):

        logout(request)

        return redirect('login')



        

    # ================= profile =================

@login_required

def profile_page(request):

        profile, created = Profile.objects.get_or_create(

            user=request.user
        )

        context = {

            'profile': profile
        }

        return render(

            request,

            'profile.html',

            context
        ) 
@login_required
def edit_profile(request):

        profile, created = Profile.objects.get_or_create(
            user=request.user
        )

        if request.method == 'POST':

            profile.phone = request.POST.get('phone')

            profile.address = request.POST.get('address')

            profile.bio = request.POST.get('bio')

            if request.FILES.get('image'):
                profile.image = request.FILES.get('image')

            profile.save()

            return redirect('profile')

        return render(
            request,
            'edit_profile.html',
            {
                'profile': profile
            }
        )


    # frontent profile
class ProfileAPIView(APIView):

        permission_classes = [
            IsAuthenticated
        ]

        def get(self, request):

            profile = request.user.profile

            return Response({

                "username":
                request.user.username,

                "email":
                request.user.email,

                "phone":
                profile.phone,

                "role":
                profile.role,

                "image":
                profile.image.url
                if profile.image
                else None,

                "address":
                profile.address,

                "bio":
                profile.bio,

            })
    # ================= JWT TEST =================

@api_view(['GET'])

@permission_classes([IsAuthenticated])

def test_api(request):

        return Response({

            "message": "JWT Working"

        })


    # ================= JWT SIGNUP =================
    # JWT SIGNUP

@api_view(['POST'])

def signup(request):

        try:

            # GET DATA
            name = request.data.get(
                'name'
            )

            email = request.data.get(
                'email'
            )

            password = request.data.get(
                'password'
            )

            # EMPTY CHECK
            if not name or not email or not password:

                return Response({

                    "message":
                    "All fields are required"

                }, status=400)

            # EMAIL EXISTS
            if User.objects.filter(
                email=email
            ).exists():

                return Response({

                    "message":
                    "Email already exists"

                }, status=400)

            # USERNAME EXISTS
            if User.objects.filter(
                username=name
            ).exists():

                return Response({

                    "message":
                    "Username already exists"

                }, status=400)

            # CREATE USER
            user = User.objects.create_user(

                username=name,

                first_name=name,

                email=email,

                password=password
            )

            # CREATE PROFILE
            Profile.objects.get_or_create(

        user=user,

        defaults={
            'role': 'user'
        }
    )

            # GENERATE JWT
            refresh = RefreshToken.for_user(
                user
            )

            # RESPONSE
            return Response({

                "token":
                str(refresh.access_token),

                "refresh":
                str(refresh),

                "user": {

                    "id":
                    user.id,

                    "name":
                    user.first_name,

                    "email":
                    user.email,

                    "role":
                    user.profile.role
                }

            })

        except Exception as e:

            return Response({

                "message":
                str(e)

            }, status=500)




    # ================= Password in small profile =================



class ChangePasswordAPIView(APIView):

        permission_classes = [
            IsAuthenticated
        ]

        def post(self, request):

            current_password = request.data.get(
                "current_password"
            )

            new_password = request.data.get(
                "new_password"
            )

            confirm_password = request.data.get(
                "confirm_password"
            )

            # CURRENT PASSWORD CHECK
            if not request.user.check_password(
                current_password
            ):

                return Response({

                    "message":
                    "Current password is incorrect"

                }, status=400)

            # PASSWORD MATCH CHECK
            if new_password != confirm_password:

                return Response({

                    "message":
                    "Passwords do not match"

                }, status=400)

            # UPDATE PASSWORD
            request.user.set_password(
                new_password
            )

            request.user.save()

            return Response({

                "message":
                "Password updated successfully"

            })

    # ================= VENUE PAGE =================

class VenueMapAPIView(APIView):
    def get(self, request):
        maps = VenueMap.objects.all()

        data = []

        for item in maps:
            data.append({
                "id": item.id,
                "venue_name": item.venue.name,
                "location": item.venue.location,
                "latitude": item.latitude,
                "longitude": item.longitude
            })

        return Response(data)
    

@api_view(['GET'])
def venue_map_api(request):
    venues = VenueMap.objects.all()
    serializer = VenueMapSerializer(
        venues,
        many=True
    )
    return Response(serializer.data)


def venue_detail(request, id):

        venue = get_object_or_404(
            Venue,
            id=id
        )

        return render(
            request,
            'venue_detail.html',
            {
                'venue': venue
            }
        )


def venues(request):

        venues = Venue.objects.all()

        return render(
            request,
            'venues.html',
            {
                'venues': venues
            }
        )



@login_required
def add_venue(request):

        if not check_permission(
            request.user,
            'manage_venues'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        if request.method == 'POST':

            name = request.POST.get('name')
            location = request.POST.get('location')
            bride_name = request.POST.get('bride_name')
            groom_name = request.POST.get('groom_name')
            status = request.POST.get('status')
            price = request.POST.get('price')
            description = request.POST.get('description')
            image = request.FILES.get('image')

            Venue.objects.create(
                name=name,
                location=location,
                bride_name=bride_name,
                groom_name=groom_name,
                status=status,
                price=price,
                description=description,
                image=image
            )

            return redirect('venues')

        return render(
            request,
            'add_venue.html'
        )
@login_required
def edit_venue(request, id):

        if not check_permission(
            request.user,
            'manage_venues'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        venue = get_object_or_404(
            Venue,
            id=id
        )

        if request.method == 'POST':

            venue.name = request.POST.get(
                'name'
            )

            venue.location = request.POST.get(
                'location'
            )

            venue.bride_name = request.POST.get(
                'bride_name'
            )

            venue.groom_name = request.POST.get(
                'groom_name'
            )
            venue.status = request.POST.get(
        'status'
    )

            venue.price = request.POST.get(
                'price'
            )

            venue.description = request.POST.get(
                'description'
            )

            if request.FILES.get('image'):

                venue.image = request.FILES.get(
                    'image'
                )

            venue.save()

            return redirect('venues')

        return render(
            request,
            'edit_venue.html',
            {
                'venue': venue
            }
        )


@login_required
def delete_venue(request, id):

        if not check_permission(
            request.user,
            'manage_venues'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        venue = get_object_or_404(
            Venue,
            id=id
        )

        venue.delete()

        return redirect('venues')


    # ================= PROTECTED VENUE API =================

@api_view(['GET'])

@permission_classes([AllowAny])
def venue_api(request):

    venues = Venue.objects.all()

    serializer = VenueSerializer(
        venues,
        many=True,
        context={"request": request}
    )

    return Response(serializer.data)

    # ================= BOOKINGS =================
@login_required
def bookings(request):

        if not check_permission(
            request.user,
            'manage_bookings'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        bookings = Booking.objects.all()

        return render(
            request,
            'bookings.html',
            {
                'bookings': bookings
            }
        )


@login_required
def my_bookings(request):

        bookings = Booking.objects.filter(
            user=request.user
        ).order_by('-created_at')

        return render(
            request,
            'my_bookings.html',
            {
                'bookings': bookings
            }
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_bookings_api(request):

        bookings = Booking.objects.filter(
            user=request.user
        ).order_by('-created_at')

        serializer = BookingSerializer(
            bookings,
            many=True
        )

        return Response(serializer.data)



    # ================= PROTECTED BOOKING API =================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def booking_api(request):

        # GET BOOKINGS
        if request.method == 'GET':

            bookings = Booking.objects.all()

            serializer = BookingSerializer(
                bookings,
                many=True
            )

            return Response(
                serializer.data
            )

        # CREATE BOOKING
        elif request.method == 'POST':

            serializer = BookingSerializer(
                data=request.data
            )

            if serializer.is_valid():

                serializer.save(
            user=request.user
        )

                return Response(
                    serializer.data
                )

            return Response(
                serializer.errors,
                status=400
            )


@login_required
def edit_booking(request, id):

        if not check_permission(
            request.user,
            'manage_bookings'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        booking = get_object_or_404(
            Booking,
            id=id
        )

        if request.method == 'POST':

            booking.customer_name = request.POST.get(
                'customer_name'
            )

            booking.customer_email = request.POST.get(
                'customer_email'
            )

            booking.customer_phone = request.POST.get(
                'customer_phone'
            )

            booking.booking_date = request.POST.get(
                'booking_date'
            )

            booking.guests = request.POST.get(
                'guests'
            )

            booking.status = request.POST.get(
                'status'
            )

            booking.save()

            return redirect('bookings')

        return render(
            request,
            'edit_booking.html',
            {
                'booking': booking
            }
        )


@login_required
def delete_booking(request, id):

        if not check_permission(
            request.user,
            'manage_bookings'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        booking = get_object_or_404(
            Booking,
            id=id
        )

        booking.delete()

        return redirect('bookings')


@login_required
def view_booking(request, id):

        if not check_permission(
            request.user,
            'manage_bookings'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        booking = get_object_or_404(
            Booking,
            id=id
        )

        return render(
            request,
            'view_booking.html',
            {
                'booking': booking
            }
        )



@login_required
def create_booking(request, venue_id):

        venue = get_object_or_404(
            Venue,
            id=venue_id
        )

        if request.method == 'POST':

            Booking.objects.create(
                user=request.user,
                venue=venue,
                customer_name=request.user.username,
                customer_email=request.user.email,
                customer_phone=request.POST.get('phone'),
                booking_date=request.POST.get('booking_date'),
                guests=request.POST.get('guests'),
                total_amount=venue.price,
                status='Pending'
            )

            messages.success(
                request,
                'Booking created successfully!'
            )

            return redirect('my_bookings')

        return render(
            request,
            'create_booking.html',
            {
                'venue': venue
            }
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_booking(request, booking_id):

        booking = get_object_or_404(
            Booking,
            id=booking_id,
            user=request.user
        )

        booking.status = 'Cancelled'

        booking.save()

        return Response({
            'message': 'Booking Cancelled Successfully'
        })





    # ================= ALL USERS =================

@login_required
def allusers(request):

        if not check_permission(
            request.user,
            'edit_users'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        search = request.GET.get('search')

        if search:
            users = User.objects.filter(
                username__icontains=search
            )
        else:
            users = User.objects.all()

        return render(
            request,
            'allusers.html',
            {
                'users': users
            }
        )

def add_user(request):

        if not check_permission(
            request.user,
            'add_users'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        if request.method == "POST":

            username = request.POST.get('username')

            email = request.POST.get('email')

            password = request.POST.get('password')

            # USERNAME EXISTS
            if User.objects.filter(
                username=username
            ).exists():

                messages.error(
                    request,
                    "Username already exists"
                )

            # EMAIL EXISTS
            elif User.objects.filter(
                email=email
            ).exists():

                messages.error(
                    request,
                    "Email already exists"
                )

            # PASSWORD EMPTY
            elif not password:

                messages.error(
                    request,
                    "Password is required"
                )

            else:

                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                messages.success(
                    request,
                    "User created successfully"
                )

                return redirect('allusers')

        return render(
            request,
            'add_user.html'
        )

@csrf_exempt
def create_payment(request):

    if request.method == "POST":

        body = json.loads(request.body)

        amount = int(body.get("amount", 0))

        client = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            )
        )

        order = client.order.create({
            "amount": amount * 100,
            "currency": "INR"
        })

        return JsonResponse(order)

    return JsonResponse(
        {"error": "Invalid request"},
        status=400
    )


@login_required
def delete_user(request, id):

        if not check_permission(
            request.user,
            'delete_users'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        user = get_object_or_404(
            User,
            id=id
        )

        # PREVENT SELF DELETE
        if request.user == user:

            messages.error(
                request,
                "You cannot delete yourself"
            )

            return redirect('allusers')

        user.delete()

        messages.success(
            request,
            "User deleted successfully"
        )

        return redirect('allusers')



@login_required
def edit_user(request, id):

        if not check_permission(
            request.user,
            'edit_users'
        ):
            messages.error(
                request,
                "Permission Denied"
            )
            return redirect('index')

        user = get_object_or_404(
            User,
            id=id
        )

        if request.method == "POST":

            user.username = request.POST.get(
                'username'
            )

            user.email = request.POST.get(
                'email'
            )

            role = request.POST.get(
                'role'
            )

            user.profile.role = role

            user.save()

            user.profile.save()

            return redirect(
                'allusers'
            )

        return render(
            request,
            'edit_user.html',
            {
                'user': user
            }
        )



    # ================= PERMISSIONS =================
def check_permission(user, permission_name):

        group_name = user.profile.role.title()

        permission = Permission.objects.filter(
            group_name=group_name   
        ).first()

        if not permission:
            return False

        return getattr(permission, permission_name, False)

def save_permission(request, group_id):

        if request.method == "POST":

            print("SAVE HIT")

            permission, created = Permission.objects.get_or_create(
                group_name=request.POST.get("group_name")
            )

            permission.add_users = 'add_users' in request.POST
            permission.edit_users = 'edit_users' in request.POST
            permission.delete_users = 'delete_users' in request.POST
            permission.manage_bookings = 'manage_bookings' in request.POST
            permission.manage_venues = 'manage_venues' in request.POST

            permission.save()

            print("SAVED")

        return redirect('allusergroups')
    # ================= USER GROUPS =================

def allusergroups(request):

        groups = UserGroup.objects.all()

        return render(
            request,
            'allusergroups.html',
            {
                'groups': groups
            }
        )


def add_allusergroups(request):

        return render(
            request,
            'add_allusergroups.html'
        )


def create_groups(request):

        if request.method == "POST":

            group_name = request.POST.get(
                'group_name'
            )

            description = request.POST.get(
                'description'
            )

            status = request.POST.get(
                'status'
            )

            UserGroup.objects.create(
                name=group_name,
                description=description,
                status=status
            )

            return redirect('allusergroups')

        return redirect(
            'add_allusergroups'
        )


def edit_allusergroups(request, id):

        group = get_object_or_404(
            UserGroup,
            id=id
        )

        permissions = Permission.objects.all()

        if request.method == 'POST':

            group.name = request.POST.get(
                'group_name'
            )

            group.description = request.POST.get(
                'description'
            )

            group.status = request.POST.get(
                'status'
            )

            group.save()

            return redirect(
                'allusergroups'
            )

        return render(
            request,
            'edit_allusergroups.html',
            {
                'group': group,
                'permissions': permissions
            }
        )


def delete_group(request, id):

        group = get_object_or_404(
            UserGroup,
            id=id
        )

        group.delete()

        return redirect(
            'allusergroups'
        )





    # ================= PAYMENTS =================

def payment_list(request):
    payments = Payment.objects.all().order_by('-payment_date')

    return render(
        request,
        'payment.html',   # <-- payment.html
        {'payments': payments}
    )

@csrf_exempt
def save_payment(request):

    if request.method == "POST":

        data = json.loads(request.body)

        wedding = Wedding.objects.get(
            id=data["wedding"]
        )

        Payment.objects.create(

            wedding=wedding,

            payer_name=data["payer_name"],

            venue_name=data["venue_name"],

            amount=data["amount"],

            razorpay_order_id=data["razorpay_order_id"],

            razorpay_payment_id=data["razorpay_payment_id"],

            payment_status="Success"
        )

        return JsonResponse({
            "message": "Payment Saved Successfully"
        })

    return JsonResponse(
        {
            "error": "Invalid Request"
        },
        status=400
    )
class WeddingListCreateView(generics.ListCreateAPIView):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class WeddingDetailView(generics.RetrieveAPIView):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer
    permission_classes = [AllowAny]            
    



def has_paid(request, wedding_id):

    username = request.GET.get("username")

    if not username:
        return JsonResponse({
            "paid": False
        })

    payment = Payment.objects.filter(
        payer_name=username,
        wedding_id=wedding_id,
        payment_status="Success"
    ).exists()

    return JsonResponse({
        "paid": payment
    })


    # =================Venue Map=================

def venue_map(request):

    if request.method == "POST":

        venue_name = request.POST.get("venue_name")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        VenueMap.objects.create(
            venue_name=venue_name,
            latitude=latitude,
            longitude=longitude
        )

        messages.success(request, "Saved Successfully")

        return redirect("venue_map")

    return render(request, "venue_map.html")
class VenueMapAPIView(APIView):

    def get(self, request):

        venues = VenueMap.objects.all()

        data = []

        for venue in venues:
            data.append({
                "id": venue.id,
                "venue_name": venue.venue_name,
                "latitude": venue.latitude,
                "longitude": venue.longitude
            })

        return Response(data)
    
# ================= BLOG PAGES =================

def blog(request):

    categories = BlogCategory.objects.all()
    form = BlogForm()

    if request.method == "POST":

        selected_category = BlogCategory.objects.get(
            id=request.POST.get("category")
        )

        Blog.objects.create(

            category=selected_category,

            title=request.POST.get("title"),

            author=request.POST.get("author"),

            image=request.FILES.get("image"),

            content=request.POST.get("content"),

            short_description=request.POST.get(
                "short_description"
            ),

            meta_title=request.POST.get(
                "meta_title"
            ),

            meta_description=request.POST.get(
                "meta_description"
            ),

            meta_keywords=request.POST.get(
                "meta_keywords"
            ),

            is_published=(
                request.POST.get("is_published") == "True"
            )
        )

        return redirect("blog")

    return render(
        request,
        "blog.html",
        {
            "categories": categories,
            "form": form
        }
    )


# BLOG LIST PAGE

def blog_list(request):

    blogs = Blog.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "blog_list.html",
        {
            "blogs": blogs
        }
    )


# DELETE BLOG

def delete_blog(request, id):

    blog = Blog.objects.get(id=id)

    blog.delete()

    return redirect(
        "blog_list"
    )


# EDIT BLOG

def edit_blog(request, id):

    blog = Blog.objects.get(id=id)

    categories = BlogCategory.objects.all()

    form = BlogForm(
        instance=blog
    )

    if request.method == "POST":

        blog.title = request.POST.get(
            "title"
        )

        blog.author = request.POST.get(
            "author"
        )

        # CKEditor content update
        blog.content = request.POST.get(
            "content"
        )

        blog.short_description = request.POST.get(
            "short_description"
        )

        blog.meta_title = request.POST.get(
            "meta_title"
        )

        blog.meta_description = request.POST.get(
            "meta_description"
        )

        blog.meta_keywords = request.POST.get(
            "meta_keywords"
        )

        blog.category = BlogCategory.objects.get(
            id=request.POST.get("category")
        )

        if request.FILES.get("image"):

            blog.image = request.FILES.get(
                "image"
            )

        blog.save()

        return redirect(
            "blog_list"
        )

    return render(
        request,
        "edit_blog.html",
        {
            "blog": blog,
            "categories": categories,
            "form": form
        }
    )


# BLOG API FOR REACT FRONTEND

def blog_api(request):

    blogs = Blog.objects.filter(
        is_published=True
    ).order_by(
        "-created_at"
    )

    data = []

    for blog in blogs:

        data.append({

            "id": blog.id,

            "title": blog.title,

            "category":
            blog.category.name
            if blog.category
            else "",

            "image":
            blog.image.url
            if blog.image
            else "",

            "short_description":
            blog.short_description,

            "slug":
            blog.slug

        })

    return JsonResponse(
        data,
        safe=False
    )


def single_blog_api(request, slug):

    blog = Blog.objects.get(
        slug=slug
    )

    data = {

        "title": blog.title,

        "category":
        blog.category.name if blog.category else "",

        "image":
        blog.image.url if blog.image else "",

        "content":
        blog.content,

        "author":
        blog.author,

        "meta_title":
        blog.meta_title,

        "meta_description":
        blog.meta_description

    }

    return JsonResponse(data)



def add_category(request):

    if request.method == "POST":

        name = request.POST.get("name")

        BlogCategory.objects.create(
            name=name
            # slug automatically save() il generate aakum
        )

        return redirect("add_category")

    return render(
        request,
        "add_category.html"
    )

    
# =================  PAGES =================

def pages(request):
    pages = Page.objects.all().order_by("nav_priority")

    return render(
        request,
        "all_pages.html",
        {
            "pages": pages
        }
    )

def add_page(request):

    if request.method == "POST":

        form = PageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("pages")

    else:
        form = PageForm()

    return render(
        request,
        "add_page.html",
        {
            "form": form,
        },
    )

def edit_page(request, id):

    page = get_object_or_404(Page, id=id)

    if request.method == "POST":

        form = PageForm(
            request.POST,
            request.FILES,
            instance=page
        )

        if form.is_valid():

            form.save()

            return redirect("pages")

    else:

        form = PageForm(instance=page)

    return render(
        request,
        "add_page.html",
        {
            "form": form,
            "page": page,
            "is_edit": True,
        },
    )
from django.shortcuts import redirect

def delete_page(request, id):

    Page.objects.get(id=id).delete()

    return redirect("pages")


def pages_api(request):

    pages = Page.objects.filter(
        status="published",
        show_in_navbar=True
    ).order_by("nav_priority")

    data = []

    for page in pages:

        data.append({
            "id": page.id,
            "page_name": page.page_name,
            "slug": page.slug,
        })

    return JsonResponse(data, safe=False)

def single_page_api(request, slug):

    page = get_object_or_404(
        Page,
        slug=slug,
        status="published"
    )

    data = {
        "id": page.id,
        "page_name": page.page_name,
        "title": page.title,
        "content": page.content,
        "meta_title": page.meta_title,
        "meta_description": page.meta_description,
        "meta_keywords": page.meta_keywords,
    }

    return JsonResponse(data)



from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

def google_login_success(request):
    if request.user.is_authenticated:
        tokens = get_tokens_for_user(request.user)

        return redirect(
            f"https://wedding-book-swart.vercel.app/google-success?access={tokens['access']}&refresh={tokens['refresh']}"
        )

    return redirect("https://wedding-book-swart.vercel.app/login")