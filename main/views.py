from django.shortcuts import render

from main.models import BackgroundSliderImage, SocialMedia, Contact, Rating, Fact, InfoCompany, Partner


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
# Create your views here.
