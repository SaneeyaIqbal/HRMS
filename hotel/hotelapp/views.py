from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HotelSerializer, ManagerSerializer, RoomSerializer, GuestSerializer, BookingSerializer
from .models import Hotel, Manager, Room, Guest, Booking


# class HotelView(viewsets.ModelViewSet):
#     serializer_class = HotelSerializer
#     queryset = Hotel.objects.all()
#

# class ManagerView(viewsets.ModelViewSet):
#     serializer_class = ManagerSerializer
#     queryset = Manager.objects.all()
#
#
# class RoomView(viewsets.ModelViewSet):
#     serializer_class = RoomSerializer
#     queryset = Room.objects.all()
#
#
# class GuestView(viewsets.ModelViewSet):
#     serializer_class = GuestSerializer
#     queryset = Guest.objects.all()
#
#
# class BookingView(viewsets.ModelViewSet):
#     serializer_class = BookingSerializer
#     queryset = Booking.objects.all()

@api_view (['GET', ])
def api_hotel_list_view(request):
    hotel = Hotel.objects.all()
    if request.method == 'GET':
        serializer = HotelSerializer(hotel, many=True)

        return Response(serializer.data)


@api_view(['GET',])
def api_hotel_details_view(request,pk):
    try:
        hotel = Hotel.objects.get(id=pk)
    except Hotel.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)


@api_view(['GET', ])
def api_manager_list_view(request):
    manager = Manager.objects.all()
    if request.method == 'GET':
        serializer = ManagerSerializer(manager,many=True)

        return Response(serializer.data)

@api_view(['GET]', ])
def api_manager_details_view(request,pk):
    try:
        manager = Manager.objects.get(id=pk)
    except Manager.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer =   ManagerSerializer(manager)
        return Response(serializer.data)

@api_view(['GET', ])
def api_room_list_view(request):
    room = Room.objects.all()
    if request.method == 'GET':
        serializer = RoomSerializer(room, many=True)

    return Response(serializer.data)

@api_view(['GET]', ])
def api_room_details_view(request,pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNOtExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RoomSerializer(room)
        return Response(serializer.data)

@api_view(['GET', ])
def api_guest_list_view(request):
    guest = Guest.objects.all()
    if request.method == 'GET':
        serializer = GuestSerializer(guest, many=True)

    return Response(serializer.data)

def api_guest_details_view(request,pk):
    try:
        guest = Guest.objects.get(id=pk)
    except Guest.DoesNOtExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)


@api_view(['GET', ])
def api_booking_list_view(request):
    booking = Booking.objects.all()
    if request.method == 'GET':
        serializer = BookingSerializer(booking, many=True)

    return Response(serializer.data)

@api_view(['GET]', ])
def api_booking_details_view(request):
    try:
        booking = Booking.objects.get(id=pk)
    except Booking.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

@api_view(['PUT', ])
def api_hotel_update_list_view(request,pk):
    try:
        hotel = Hotel.objects.get(id=pk)
    except Hotel.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = HotelSerializer(hotel,data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = "Update Successful"
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT', ])
def api_manager_update_list_view(request,pk):
    try:
        manager = Manager.objects.get(id=pk)
    except Manager.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ManagerSerializer(manager,data=request.data)

        if serializer.is_valid():
            serializer.save()
            data={}
            data['success'] = "Update Successfull"
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT', ])
def api_room_update_list_view(request,pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RoomSerializer(room,data=request.data)

        if serializer.is_valid():
            serializer.save()
            data={}
            data['success'] = "Update Successfull"
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT', ])
def api_guest_update_list_view(request,pk):
    try:
        guest = Guest.objects.get(id=pk)
    except Guest.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = GuestSerializer(guest,data=request.data)

        if serializer.is_valid():
            serializer.save()
            data={}
            data['success'] = "Update Successfull"
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT', ])
def api_booking_update_list_view(request,pk):
    try:
        booking = Booking.objects.get(id=pk)
    except Booking.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BookingSerializer(booking,data=request.data)

        if serializer.is_valid():
            serializer.save()
            data={}
            data['success'] = "Update Successfull"
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST', ])
def api_hotel_post_view(request):
    if request.method == 'POST':
        serializer = HotelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success']="Update Successful"
            return Response(serializer.data)
        return Response(status.HTTP_201_CREATED)


@api_view(['POST', ])
def api_manager_post_view(request):
    if request.method == 'POST':
        serializer = ManagerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success']="Update Successful"
            return Response(serializer.data)
        return Response(status.HTTP_201_CREATED)

@api_view(['POST', ])
def api_room_post_view(request):
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success']="Update Successful"
            return Response(serializer.data)
        return Response(status.HTTP_201_CREATED)


@api_view(['POST', ])
def api_guest_post_view(request):
    if request.method == 'POST':
        serializer = GuestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success']="Update Successful"
            return Response(serializer.data)
        return Response(status.HTTP_201_CREATED)

@api_view(['POST', ])
def api_booking_post_view(request):
    if request.method == 'POST':
        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success']="Update Successful"
            return Response(serializer.data)
        return Response(status.HTTP_201_CREATED)

@api_view(['DELETE', ])
def api_hotel_delete_view(request,pk):
    try:
        hotel = Hotel.objects.get(id=pk)
    except Hotel.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = hotel.delete()
        data = {}
        if operation:
            data['success']= "Delete Succesfull"
        else:
            data['failure']= "Unsuccessfull"
            return Response(data,status.HTTP_200_OK)
        return Response(data,status.HTTP_404_NOT_FOUND)

@api_view(['DELETE', ])
def api_manager_delete_view(request,pk):
    try:
        manager = Manager.objects.get(id=pk)
    except Hotel.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = manager.delete()
        data = {}
        if operation:
            data['success']= "Delete Succesfull"
        else:
            data['failure']= "Unsuccessfull"
            return Response(data,status.HTTP_200_OK)
        return Response(data,status.HTTP_404_NOT_FOUND)

@api_view(['DELETE', ])
def api_room_delete_view(request,pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = room.delete()
        data = {}
        if operation:
            data['success']= "Delete Succesfull"
        else:
            data['failure']= "Unsuccessfull"
            return Response(data,status.HTTP_200_OK)
        return Response(data,status.HTTP_404_NOT_FOUND)

@api_view(['DELETE', ])
def api_guest_delete_view(request,pk):
    try:
        guest = Guest.objects.get(id=pk)
    except Guest.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = guest.delete()
        data = {}
        if operation:
            data['success']= "Delete Succesfull"
        else:
            data['failure']= "Unsuccessfull"
            return Response(data,status.HTTP_200_OK)
        return Response(data,status.HTTP_404_NOT_FOUND)

@api_view(['DELETE', ])
def api_booking_delete_view(request,pk):
    try:
        booking = Booking.objects.get(id=pk)
    except Booking.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = booking.delete()
        data = {}
        if operation:
            data['success']= "Delete Succesfull"
        else:
            data['failure']= "Unsuccessfull"
            return Response(data,status.HTTP_200_OK)
        return Response(data,status.HTTP_404_NOT_FOUND)