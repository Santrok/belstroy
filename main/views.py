from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from main.models import BackgroundSliderImage, SocialMedia, Contact, Rating, Fact, InfoCompany, Partner, HouseType, \
    House, SignUpForAFreeConsultation, CallBack, Improvement, Review, Vacancy
from main.serializer import HouseTypeSerializer, HouseAllSerializer, ConsultationSerializer, CallBackSerializer, ImprovementDetailSerializer, \
    ImprovementSerializer
from main.services import send_telegram_message


def get_main_page(request):
    slider_photo = BackgroundSliderImage.objects.all()
    social_account = SocialMedia.objects.all()
    contact = Contact.objects.first()
    rating = Rating.objects.first()
    facts = Fact.objects.all()
    company_info = InfoCompany.objects.first()
    partners = Partner.objects.all()
    reviews = Review.objects.filter(is_publish=True)
    vacancy = Vacancy.objects.filter(is_publish=True)

    context = {
        "slider_photo": slider_photo,
        "social_account": social_account,
        "contact": contact,
        "rating": rating,
        "facts": facts,
        "company_info": company_info,
        "partners": partners,
        "reviews": reviews,
        "vacancy": vacancy,
    }
    return render(request, 'index.html', context)


class MaterialHouseAPIView(ListAPIView):
    queryset = HouseType.objects.all()
    serializer_class = HouseTypeSerializer


class DetailHouseAPIView(RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseAllSerializer


class ConsultationAPIView(CreateAPIView):
    queryset = SignUpForAFreeConsultation
    serializer_class = ConsultationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        message = (f'Заявка на консультацию:\n Имя: {serializer.validated_data.get("name")}\n'
                   f'Телефон: {serializer.validated_data.get("phone_number")}\n'
                   f' Дата консультации: {serializer.validated_data.get("date_of_consultation")}')
        send_telegram_message(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CallBackAPIView(CreateAPIView):
    queryset = CallBack
    serializer_class = CallBackSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        message = (f'Заявка на обратный звонок:\n Имя: {serializer.validated_data.get("name")}\n'
                   f'Телефон: {serializer.validated_data.get("phone_number")}')
        send_telegram_message(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ImprovementAPIView(ListAPIView):
    queryset = Improvement.objects.all()
    serializer_class = ImprovementSerializer


class ImprovementDetailAPIView(RetrieveAPIView):
    queryset = Improvement.objects.all()
    serializer_class = ImprovementDetailSerializer

