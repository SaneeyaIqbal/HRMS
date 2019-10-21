from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HotelSerializer, ManagerSerializer, RoomSerializer, GuestSerializer, BookingSerializer
from .models import Hotel, Manager, Room, Guest, Booking


class HotelView(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class ManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()


class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class GuestView(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


