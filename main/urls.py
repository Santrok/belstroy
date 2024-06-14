from django.urls import path

from main.views import get_main_page, MaterialHouseAPIView, DetailHouseAPIView

urlpatterns = [
    path('', get_main_page),
    path('api/material/', MaterialHouseAPIView.as_view()),
    path('api/house_detail/<int:pk>/', DetailHouseAPIView.as_view())
]
