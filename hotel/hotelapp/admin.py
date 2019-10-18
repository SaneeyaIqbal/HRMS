from django.contrib import admin
from django import forms

from .models import Hotel,Manager,Room,Guest,Booking

class HotelAdmin(admin.ModelAdmin):
    list_display = ('Name','City',)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('Name','Number',)

# class TypeAdmin(admin.ModelAdmin):
#     list_display = ('Type_1','Type_2','Type_3',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('Number','Type','Bed','Price','Availability',)

class GuestAdmin(admin.ModelAdmin):
    list_display = ('Name','Number','Address',)


# class BookingAdminForm(forms.ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super(BookingAdminForm, self).__init__(*args, **kwargs)
#
#     def clean(self):
#         room = self.cleaned_data.get('room')
#         is_available = self.cleaned_data.get('is_available')
#         if not is_available:
#             if room.Available == 0:
#                 raise forms.ValidationError("Room is not available",code="invalid")
#             return self.cleaned.data
#
#     def save(self, commit=True):
#         return super(BookingAdminForm, self).save(commit)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('Guest_Name','Guests','date_of_book','date_of_cancel',
                    'Check_IN','Check_OUT','bill','checked_out','Room_Number',)
    #form = BookingAdminForm

# class BillAdmin(admin.ModelAdmin):
#     list_display = ('Check_IN','Guest_Name','Type','Check_OUT','Invoice',)


# Register your models here.
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Manager,ManagerAdmin)
#admin.site.register(Room_Type,TypeAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Guest,GuestAdmin)
admin.site.register(Booking,BookingAdmin)
#admin.site.register(Bill,BillAdmin)





