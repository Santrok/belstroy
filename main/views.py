from django.shortcuts import render

from main.models import BackgroundSliderImage, SocialMedia, Contact


def get_main_page(request):
    slider_photo = BackgroundSliderImage.objects.all()
    social_account = SocialMedia.objects.all()
    contact = Contact.objects.filter()[1:]

    context = {
        "slider_photo": slider_photo,
        "social_account": social_account,
        "contact": contact,
    }
    return render(request, 'index.html', context)
# Create your views here.
