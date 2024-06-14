import telebot
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from config.settings import env_keys
from main.models import BackgroundSliderImage, SocialMedia, Contact, Rating, Fact, InfoCompany, Partner, HouseType, \
    House, SignUpForAFreeConsultation, CallBack
from main.serializer import HouseTypeSerializer, HouseAllSerializer, ConsultationSerializer, CallBackSerializer


def get_main_page(request):
    slider_photo = BackgroundSliderImage.objects.all()
    social_account = SocialMedia.objects.all()
    contact = Contact.objects.first()
    rating = Rating.objects.first()
    facts = Fact.objects.all()
    company_info = InfoCompany.objects.first()
    partners = Partner.objects.all()

    context = {
        "slider_photo": slider_photo,
        "social_account": social_account,
        "contact": contact,
        "rating": rating,
        "facts": facts,
        "company_info": company_info,
        "partners": partners,
    }
    return render(request, 'index.html', context)


def send_telegram_message(message):
    """ Отправляем сообщение в чат бота """
    bot_token = env_keys.get('BOT_TOKEN')
    chat_id = env_keys.get('BOT_CHAT_ID')
    bot = telebot.TeleBot(bot_token)
    bot.send_message(chat_id, message)



class MaterialHouseAPIView(ListAPIView):
    queryset = HouseType.objects.all()
    serializer_class = HouseTypeSerializer


class DetailHouseAPIView(RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseAllSerializer


class ConsultationAPIView(CreateAPIView):
    queryset = SignUpForAFreeConsultation
    serializer_class = ConsultationSerializer


class CallBackAPIView(CreateAPIView):
    queryset = CallBack
    serializer_class = CallBackSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        message = f'Имя: {serializer.validated_data.get("name")}\nТелефон: {serializer.validated_data.get("phone_number")}'
        send_telegram_message(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)