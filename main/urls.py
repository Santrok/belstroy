from django.urls import path

from main.views import get_main_page, MaterialHouseAPIView, DetailHouseAPIView, ConsultationAPIView, CallBackAPIView, \
    ImprovementAPIView

urlpatterns = [
    path('', get_main_page),
    path('api/material/', MaterialHouseAPIView.as_view()),
    path('api/house_detail/<int:pk>/', DetailHouseAPIView.as_view()),
    path('api/create_consultation/', ConsultationAPIView.as_view()),
    path('api/create_callback/', CallBackAPIView.as_view()),
    path('api/improvement/', ImprovementAPIView.as_view()),
]
