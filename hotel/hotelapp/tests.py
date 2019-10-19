from django.test import TestCase
from .models import Hotel,Manager,Room,Booking

# Create your tests here.

class HotelTestCase(TestCase):
    def setUp(self):
        Hotel.objects.create(name = "ABC")

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


# class RoomTestCase(TestCase):
#     def setUp(self):
#         Room.objects.create(number = 101)
#         Room.objects.create(bed = 1)
#
#     def test_case_room_title(self):
#         num = Room.objects.get(number = 101)
#         num_of_bed = Room.objects.get(bed = 3)
#         self.assertEqual(num.get_room_number(),101)
#         self.assertEqual(num_of_bed.get_bed(), 3)

class BookingTestCase(TestCase):
    def setUp(self):
        Booking.objects.create(guests=3)

    def test_case_booking_deatils(self):
        book = Booking.objects.get(guests=3)
        self.assertEqual(book.get_detail(),3)
#
