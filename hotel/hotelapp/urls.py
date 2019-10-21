from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('hotels', views.HotelView) #GET, POST, PUT, DELETE, HEAD, OPTIONS
# router.register('hotels', views.ManagerView)
# router.register('hotels', views.GuestView)
# router.register('hotels', views.RoomView)
router.register('hotels', views.BookingView)


urlpatterns = [
    path('', include(router.urls)),
]