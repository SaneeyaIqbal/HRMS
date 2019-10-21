from django.test import TestCase
from .models import *
from datetime import date


# Create your tests here.

class HotelTestCase(TestCase):
    def setUp(self):
        Hotel.objects.create(name="ABC")

    def test_case_hotel_correct_title(self):
        a = Hotel.objects.get(name="ABC")
        self.assertEqual(a.get_title(),"ABC")


class ManagerTestCase(TestCase):
    def setUp(self):
        Manager.objects.create(name="brettMard")
        Manager.objects.create(name="willey")

    def test_case_manager_correct_title(self):
        brettMard = Manager.objects.get(name="brettMard")
        willey = Manager.objects.get(name="willey")
        self.assertEqual(brettMard.get_name(), "brettMard")
        self.assertEqual(willey.get_name(), "willey")


class RoomTestCase(TestCase):
    def setUp(self):
        Room.objects.create(number=101, type='A')

    def test_case_find_room_price(self):
        room = Room.objects.get(number=101)
        self.assertEqual(room.room_price(), 1000)


class BookingTestCase(TestCase):

    def setUp(self):
        room_number = Room.objects.create(number=101, type='A')
        guest_name = Guest.objects.create(name='Saniya', address='Tumkur', number='1234567890')
        Booking.objects.create(number=room_number, name=guest_name, guests=3, check_in='2019-10-20')

    def test_case_check_out_date(self):

        guest_name = Guest.objects.get(name='Saniya',number='1234567890',address='Tumkur')
        booking = Booking.objects.get(guest=guest_name)
        self.assertEqual(booking.check_out_date(),date(2019,10,22))

    def test_case_booking_room_number(self):

        guest_name = Guest.objects.get(name='Saniya', address='Tumkur', number='1234567890')
        booking = Booking.objects.get(guest=guest_name)
        self.assertEqual(booking.room_number(), 101)

    def test_case_booking_room_type(self):

        guest_name = Guest.objects.get(name='Saniya', address='Tumkur', number='1234567890')
        booking = Booking.objects.get(guest=guest_name)
        self.assertEqual(booking.room_type(), 'A')

    def test_case_booking_room_price_per_night(self):

        guest_name = Guest.objects.get(name='Saniya', address='Tumkur', contact_number='1234567890')
        booking = Booking.objects.get(guest=guest_name)
        self.assertEqual(booking.room_price(), 1000)

    def test_case_guest_name(self):

        guest_name = Guest.objects.get(name='Saniya', address='Tumkur', contact_number='1234567890')
        booking = Booking.objects.get(guest=guest_name)
        self.assertEqual(booking.guest_name_detail(), 'Saniya')

    def test_case_contact_number(self):

        guest_name = Guest.objects.get(name='Saniya', address='Tumkur', contact_number='1234567890')
        booking = Booking.objects.get(guest=guest_name)
        self.assertEqual(booking.contact_number(), '1234567890')

    def test_case_cost_of_stay(self):

        guest_name = Guest.objects.get(name='Saniya', address='Tumkur', contact_number='1234567890')
        booking = Booking.objects.get(guest=guest_name)
        self.assertEqual(booking.cost(), 1000)