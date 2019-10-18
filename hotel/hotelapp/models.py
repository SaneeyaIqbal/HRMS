from django.db import models
from datetime import date, timedelta, datetime
from django.db.models import signals
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

#Create your models here.

class Hotel(models.Model):
    Name = models.CharField(max_length=20)
    City = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Name)

class Manager(models.Model):
    Name = models.CharField(max_length=20)
    Number = models.IntegerField()

    def __str__(self):
        return str(self.Name)

# class Room_Type(models.Model):
#     Type_1 = models.CharField(max_length=20)
#     Type_2 = models.CharField(max_length=20)
#     Type_3 = models.CharField(max_length=20)

    # def __str__(self):
    #     return str(self.Type_1) + str(self.Type_2) + str(self.Type_3)

class Room(models.Model):
    Number = models.IntegerField()
    Type = models.CharField(max_length=20)
    Bed = models.IntegerField()
    Price = models.IntegerField()
    Availability = models.BooleanField()


    def __str__(self):
        return str(self.Type)

    def checked_out(self):
        if self.Number > 0:
            return True
        else:
            return False

    checked_out.boolean = True
    checked_out.short_description = 'checked_out'


class Guest(models.Model):
    Name = models.CharField(max_length=20)
    Number = models.IntegerField()
    Address = models.TextField()

    def __str__(self):
        return str(self.Name)

class Booking(models.Model):
    Guest_Name = models.ForeignKey(Guest, on_delete=models.CASCADE)
    Room_Number = models.ForeignKey(Room, on_delete=models.CASCADE)
    # Type = models.ForeignKey(Room,on_delete=models.CASCADE)
    Guests = models.IntegerField()
    date_of_book = models.DateField()
    date_of_cancel = models.DateField(null=True,blank=True)
    Check_IN = models.DateField()
    Check_OUT = models.DateField()
    # Invoice = models.IntegerField(default=0)
    #Available = models.IntegerField()
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Guest_Name)

    def bill(self):
        if self.checked_out:
            timedelta1 = self.Check_OUT - self.Check_IN
            days = timedelta1.days
            return days * self.Room_Number.Price


        # if self.Check_IN is not None:
        #     self.Invoice = self.Check_OUT - self.Check_IN
        #     if self.Invoice.days > 0:
        #         return self.Invoice.days * self.Type.Price
        #     else:
        #         return 0

@receiver(signals.post_save,sender=Booking)
def update(sender,instance,created,**kwargs):
    if not instance.Check_OUT:
        if created:
            avail = instance.Check_IN.Availability
            if avail > 0:
                avail -= 1
                room = instance.Check_IN
                room.Availability = avail
                if avail <= 0:
                    room.availability = False
                room.save()

        else:
            avail = instance.Check_IN.Availability
            room = instance.Check_IN
            room.availability = avail + 1
            room.save()















# class Bill(models.Model):
#
#     Guest_Name = models.ForeignKey(Guest, on_delete=models.CASCADE)
#     Type = models.ForeignKey(Room, on_delete=models.CASCADE)
#
#
#     def __str__(self):
#         return str(self.Guest_Name)






















# + self.Number
# + self.Number + str(self.Address)
# + str(self.Type) + str(self.Bed) + self.Price + self.Availability
#  + str(self.Type2) + str(self.Type3)
# + str(self.Type) + str(self.Guests) + self.date_of_book + self.date_of_cancel
# + str(self.Type) + str(self.Bed) + \
               # str(self.Price) + str(self.Availability)