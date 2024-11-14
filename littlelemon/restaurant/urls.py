from django.contrib import admin 
from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token
from . import views
  
urlpatterns = [ 
    path('menu/', views.MenuItemView.as_view(), name='menu_items'),  # Listeleme ve oluşturma
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('menu-items/', views.ListCreateMenuItemView.as_view(), name='menu-list-create'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('menu-items/', views.MenuItemsView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]