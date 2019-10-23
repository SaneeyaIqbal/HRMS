from django.urls import path, include
from .views import api_hotel_list_view,api_hotel_details_view,api_manager_list_view,api_manager_details_view,api_room_list_view,api_room_details_view,api_guest_list_view,api_guest_details_view,api_booking_list_view,api_booking_details_view,api_hotel_update_list_view,\
   api_hotel_update_list_view,api_room_update_list_view,api_manager_update_list_view,api_guest_update_list_view,api_booking_update_list_view,\
   api_hotel_post_view,api_manager_post_view,api_room_post_view,api_guest_post_view,api_booking_post_view,\
   api_hotel_delete_view,api_manager_delete_view,api_room_delete_view,api_guest_delete_view,api_booking_delete_view

from rest_framework import routers
from . import views
from .models import *

# router = routers.DefaultRouter()
# router.register('hotels', views.HotelView) #GET, POST, PUT, DELETE, HEAD, OPTIONS
# # router.register('hotels', views.ManagerView)
# # router.register('hotels', views.GuestView)
# # router.register('hotels', views.RoomView)
# router.register('hotels', views.BookingView)
app_name = 'hotelapp'

urlpatterns = [
   #path('', api_hotel_list_view, name='hotel_list'),
   path('',api_guest_list_view,name='guest_list'),
   # path('<pk>/',api_hotel_details_view, name= 'hotel_detail'),
   # path('<pk>/update/',api_hotel_update_list_view,name='hotel_update'),
   # path('create/',api_hotel_post_view,name='hotel_post'),
   # path('<pk>/delete',api_hotel_delete_view,name='hotel_delete'),
   path('create/',api_guest_post_view,name='guest_create'),
]