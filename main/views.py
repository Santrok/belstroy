from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView

from main.models import BackgroundSliderImage, SocialMedia, Contact, Rating, Fact, InfoCompany, Partner, HouseType, \
    House
from main.serializer import HouseTypeSerializer, HouseAllSerializer


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


class MaterialHouseAPIView(ListAPIView):
    queryset = HouseType.objects.all()
    serializer_class = HouseTypeSerializer


class DetailHouseAPIView(RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseAllSerializer
