from django.contrib import admin
from django import forms

from .models import Hotel,Manager,Room,Guest,Booking

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','city',)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name','number',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('number','type','bed','price','availability',)
    ordering = ('number',)

class GuestAdmin(admin.ModelAdmin):
    list_display = ('name','number','address',)
    ordering = ('name',)

class BookingAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookingAdminForm, self).__init__(*args, **kwargs)
        if not self.instance.id:
            self.fields['checked_out'].disabled = True
            self.fields['is_cancel'].disabled = True
        if self.instance.id:
            self.fields['room_number'].disabled = True
            self.fields['guest_name'].disabled = True
            self.fields['check_in'].disabled = True
            self.fields['guests'].disabled = True
        if self.instance.checked_out or self.instance.is_cancel:
            self.fields['checked_out'].disabled = True
            self.fields['is_cancel'].disabled = True

    def clean(self):
        guests = self.cleaned_data.get('guests')
        available = self.cleaned_data.get('available')
        check_in = self.cleaned_data.get('check_in')
        check_out = self.cleaned_data.get('check_out')
        date_of_book = self.cleaned_data.get('date_of_book')
        checked_out = self.cleaned_data.get('checked_out')
        is_cancel = self.cleaned_data.get('is_cancel')
        number = self.cleaned_data.get('room_number')
        guest_name = self.cleaned_data.get('guest_name')

        # if number.availability:
        #     raise forms.ValidationError("You can't book another room.")

        if check_out < check_in:
            raise forms.ValidationError("invalid dates", code="invalid")

        if guests > 3:
            raise forms.ValidationError("Only three Guests can accommodate", code="invalid")

        bookings = Booking.objects.filter(room_number=number, check_in=check_in, check_out=check_out)

        if len(bookings) > 0:
            raise forms.ValidationError("Room unavailable", code="invalid")

    def save(self, commit=True):
        return super(BookingAdminForm, self).save(commit=commit)









class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','guest_name','guests','date_of_book','is_cancel',
                    'check_in','check_out','bill','checked_out','room_number',)
    ordering = ('id',)
    form = BookingAdminForm


# Register your models here.
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Manager,ManagerAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Guest,GuestAdmin)
admin.site.register(Booking,BookingAdmin)


# guest = self.cleaned_data.get('guest')
# bookings = Booking.objects.all()
# all_guests = []
# for i in bookings:
#     all_guests.append(i.guest)
# if guest not in all_guests or guest in all_guests:
#     if room.available == False:
#         raise forms.ValidationError("Room is not available, please change the room number", code='invalid')
# else:
#     raise forms.ValidationError("You can't book another room.")



 # if str(guest_name) == str(guest_name.name):
        #     raise forms.ValidationError("Guest can book only one room at a time", code="invalid")



        # booking_obj = Booking.objects.filter(checked_out=False).filter(is_cancel=False)
        # for obj in booking_obj:
        #     value = obj

        # if str(bookings.guest_name) == str(guest_name.name):
        #     raise forms.ValidationError("Guest can book only one room at a time", code="invalid")


# bookings = Booking.objects.all()
# all_guests = []
# for i in bookings:
#     all_guests.append(i.guest_name)
# if guest_name not in all_guests or guest_name in all_guests:

#         raise forms.ValidationError("Room is not available, please change the room number", code='invalid')
# else:
