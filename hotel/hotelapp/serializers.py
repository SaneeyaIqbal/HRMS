from rest_framework import serializers
from .models import Hotel, Manager, Room, Guest, Booking


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'url', 'name', 'city', )


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'name', 'number', )


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('number', 'type', 'bed', 'price', 'avalability', )


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('name', 'number', 'address', )


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'guest_name', 'room_number', 'number_of_stay_days', 'guests',
                  'date_of_book', 'is_cancel', 'check_in', 'check_out', 'checked_out', )


