from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Menu
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(name="Pizza", price=10.99, description="Cheesy pizza")
        self.menu2 = Menu.objects.create(name="Burger", price=5.99, description="Beef burger")
        self.menu3 = Menu.objects.create(name="Pasta", price=8.99, description="Creamy pasta")

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)