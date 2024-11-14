from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu, Booking, MenuItem
from  django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuSerializer, BookingSerializer, MenuItemSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class MenuItemView(generics.ListCreateAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
      permission_classes = [IsAuthenticated]
      queryset = Booking.objects.all()
      serializer_class = BookingSerializer
      
class ListCreateMenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
 return Response({"message":"This view is protected"})