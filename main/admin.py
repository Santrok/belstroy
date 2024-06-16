from django.contrib import admin

from main.models import BackgroundSliderImage, ImprovementPhoto, SocialMedia, Contact, Rating, InfoCompany, Fact, Partner, HouseType, \
    House, HousePlanPhoto, HouseFacadePhoto, HouseSectionPhoto, HousePhoto, SignUpForAFreeConsultation, CallBack, \
    Improvement, Review

# Register your models here.
admin.site.register(BackgroundSliderImage)
admin.site.register(SocialMedia)
admin.site.register(Contact)
admin.site.register(Rating)
admin.site.register(InfoCompany)
admin.site.register(Fact)
admin.site.register(Partner)
admin.site.register(HouseType)
admin.site.register(House)
admin.site.register(HousePlanPhoto)
admin.site.register(HouseFacadePhoto)
admin.site.register(HouseSectionPhoto)
admin.site.register(HousePhoto)
admin.site.register(SignUpForAFreeConsultation)
admin.site.register(CallBack)
admin.site.register(Improvement)
admin.site.register(ImprovementPhoto)
admin.site.register(Review)