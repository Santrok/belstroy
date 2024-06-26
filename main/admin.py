from django.contrib import admin

from main.models import BackgroundSliderImage, ImprovementPhoto, SocialMedia, Contact, Rating, InfoCompany, Fact, \
    Partner, HouseType, \
    House, HousePlanPhoto, HouseFacadePhoto, HousePhoto, SignUpForAFreeConsultation, CallBack, \
    Improvement, Review, Vacancy, AdminHouse, AdminHousePhoto, AdminContact, AdminSignUpForAFreeConsultation, \
    AdminVacancy, AdminInfoCompany, AdminCallBack, AdminBackgroundSliderImage, AdminImprovement, AdminReview

# Register your models here.
admin.site.register(BackgroundSliderImage, AdminBackgroundSliderImage)
admin.site.register(SocialMedia)
admin.site.register(Contact, AdminContact)
admin.site.register(Rating)
admin.site.register(InfoCompany, AdminInfoCompany)
admin.site.register(Fact)
admin.site.register(Partner)
admin.site.register(HouseType)
admin.site.register(House, AdminHouse)
# admin.site.register(HousePlanPhoto)
# admin.site.register(HouseFacadePhoto)
# admin.site.register(HousePhoto, AdminHousePhoto)
admin.site.register(SignUpForAFreeConsultation, AdminSignUpForAFreeConsultation)
admin.site.register(CallBack, AdminCallBack)
admin.site.register(Improvement, AdminImprovement)
admin.site.register(ImprovementPhoto)
admin.site.register(Review, AdminReview)
admin.site.register(Vacancy, AdminVacancy)