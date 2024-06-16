from django.contrib import admin
from django.db import models

# Create your models here.


class HousePlanPhoto(models.Model):
    photo = models.ImageField('Изображение плана дома', upload_to='house_plan_photos')
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    def __str__(self):
        return self.house.name


class AdminHousePlanPhoto(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: HousePlanPhoto"""


class HouseFacadePhoto(models.Model):
    photo = models.ImageField('Изображение фасада дома', upload_to='house_facade_photos')
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    def __str__(self):
        return self.house.name


class AdminHouseFacadePhoto(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: HouseFacadePhoto"""


class HouseSectionPhoto(models.Model):
    photo = models.ImageField('Изображение дома в разрезе', upload_to='house_section_photos')
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    def __str__(self):
        return self.house.name


class AdminHouseSectionPhoto(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: HouseSectionPhoto"""


class HousePhoto(models.Model):
    photo = models.ImageField('Изображение', upload_to='house_photos')
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    def __str__(self):
        return self.house.name


class AdminHousePhoto(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: HousePhoto"""


class HouseType(models.Model):
    material = models.CharField('Материал стен', max_length=255)

    def __str__(self):
        return self.material


class AdminHouseType(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: HouseType"""


class House(models.Model):
    name = models.CharField('Название дома', max_length=500, blank=True, null=True)
    facade = models.CharField('Фасад', max_length=500, blank=True, null=True)
    square = models.CharField('Площадь', max_length=500, blank=True, null=True)
    room = models.CharField('Количество комнат', max_length=500, blank=True, null=True)
    bathroom = models.CharField('Количество санузлов', max_length=500, blank=True, null=True)
    floor = models.CharField('Количество этажей', max_length=500, blank=True, null=True)
    description = models.TextField('Описание дома', blank=True, null=True)
    material = models.ForeignKey('HouseType', on_delete=models.CASCADE, verbose_name='Материал стен', blank=True, null=True)
    main_photo = models.ImageField('Главное изображение', upload_to='house_main_photos', blank=True, null=True)
    cost_of_basic_equipment = models.CharField('Стоимость базовой комплектации', max_length=255, blank=True, null=True)
    building_materials_equipment = models.CharField("Стоимость стройматериалов", max_length=255, blank=True, null=True)
    link_to_video_on_youtube = models.CharField("Ссылка на видео в YouTub", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class AdminHouse(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: House"""


class Contact(models.Model):
    address = models.CharField('Адрес', max_length=1000, blank=True, null=True)
    floor = models.CharField('Этаж', max_length=1000, blank=True, null=True)
    working_days = models.CharField("Рабочие дни", max_length=255, blank=True, null=True)
    working_hours = models.CharField('Время работы', max_length=500, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    phone_number = models.CharField('Номер телефона', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.address


class AdminContact(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Contact"""


class SocialMedia(models.Model):
    title_social_media = models.CharField('Социальная сеть', max_length=500)
    link = models.CharField("Ссылка", max_length=500, blank=True, null=True)
    phone_number = models.CharField('Номер телефона', max_length=255, blank=True, null=True)
    image = models.FileField('Иконка', upload_to='social_images')

    def __str__(self):
        return self.title_social_media


class AdminSocialMedia(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: SocialMedia"""


class Partner(models.Model):
    title_partner = models.CharField('Имя партнера', max_length=500)
    image = models.ImageField('Изображение', upload_to='partner_images')

    def __str__(self):
        return self.title_partner


class AdminPartner(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Partner"""


class Rating(models.Model):
    rating = models.CharField("Рейтинг", max_length=10)

    def __str__(self):
        return self.rating


class SignUpForAFreeConsultation(models.Model):
    name = models.CharField("Имя", max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255)
    date_of_consultation = models.DateField("Дата")
    application_processed = models.BooleanField("Заявка обработана", default=False)

    def __str__(self):
        return f'{self.name} {self.date_of_consultation} {self.phone_number}'


class AdminSignUpForAFreeConsultation(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: SignUpForAFreeConsultation"""


class Fact(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    fact_description = models.CharField("Текст", max_length=500)

    def __str__(self):
        return self.title


class AdminFact(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Fact"""


class InfoCompany(models.Model):
    years_on_the_market = models.IntegerField("Лет на рынке недвижимости")
    satisfied_clients = models.IntegerField("Довольных клиентов")
    number_of_reviews = models.IntegerField("Количество отзывов")
    the_number_of_employees = models.IntegerField("Количество сотрудников")

    def __str__(self):
        return "Информация о компании"


class AdminInfoCompany(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: InfoCompany"""


class CallBack(models.Model):
    name = models.CharField("Имя", max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255, blank=True, null=True)
    application_date = models.DateTimeField("Дата заявки", auto_now_add=True)
    application_processed = models.BooleanField("Заявка обработана", default=False)

    def __str__(self):
        return f'{self.name} {self.phone_number}'


class AdminCallBack(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: CallBack"""


class BackgroundSliderImage(models.Model):
    image = models.ImageField('Изображение', upload_to='background_images')

    def __str__(self):
        return f'{self.image}'

class AdminBackgroundSliderImage(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: BackgroundSliderImage"""


class ImprovementPhoto(models.Model):
    photo = models.ImageField('Изображение', upload_to="improvement_photos")
    improvement = models.ForeignKey('Improvement', on_delete=models.CASCADE, verbose_name='Благоустройство')

    def __str__(self):
        return self.improvement.title


class Improvement(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание")
    main_photo = models.ImageField("Главное изображение", upload_to="improvement_main_photo")
    
    def __str__(self):
        return self.title


class AdminImprovement(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Improvement"""


class Review(models.Model):
    name = models.CharField("Имя человека оставившего отзыв", max_length=255)
    city_expert_level = models.CharField("Уровень знатока города", max_length=255)
    description = models.TextField("Текст отзыва")
    photo = models.ImageField("Изображение", upload_to="reviews_photo")
    is_publish = models.BooleanField("Опубликовано", default=False)

    def __str__(self):
        return self.name

class AdminReview(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Review"""



# class ImprovementPhoto(models.Model):
#     photo = models.ImageField('Изображение')
#     improvement = models.ForeignKey('Благоустройство', on_delete=models.CASCADE, verbose_name='Дом')
#
#     def __str__(self):
#         return self.improvement.name
#
#
# class Improvement(models.Model):
#     name = models.CharField('Название дома', max_length=500, blank=True, null=True)
#     facade = models.CharField('Фасад', max_length=500, blank=True, null=True)
#     square = models.CharField('Площадь', max_length=500, blank=True, null=True)
#     room = models.CharField('Количество комнат', max_length=500, blank=True, null=True)
#     bathroom = models.CharField('Количество санузлов', max_length=500, blank=True, null=True)
#     floor = models.CharField('Количество этажей', max_length=500, blank=True, null=True)
#     description = models.TextField('Описание дома', blank=True, null=True)
#     material = models.ForeignKey('HouseType', on_delete=models.CASCADE, verbose_name='Материал стен', blank=True, null=True)
#     main_photo = models.ImageField('Главное изображение', blank=True, null=True)
#     cost_of_basic_equipment = models.CharField('Стоимость базовой комплектации', max_length=255, blank=True, null=True)
#     building_materials_equipment = models.CharField("Стоимость стройматериалов", max_length=255, blank=True, null=True)
#
#     def __str__(self):
#         return self.name
