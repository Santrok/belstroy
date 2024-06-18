from django.contrib import admin
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.


class HousePlanPhoto(models.Model):
    photo = models.FileField('Изображение плана дома',
                              upload_to='house_plan_photos',
                              help_text='Изображение должно быть в формате avif, '
                                        'преобразовать можно '
                                        '<a href="https://imagetostl.com/ru/convert/file/jpg/to/avif" target="_blank">тут</a>',
                              validators=[FileExtensionValidator(['avif'])])
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    class Meta:
        verbose_name = "Изображение плана проекта (дома)"
        verbose_name_plural = "Изображения плана проекта (дома)"

    def __str__(self):
        return self.house.name


class AdminHousePlanPhoto(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: HousePlanPhoto"""


class HousePlanPhotoInlines(admin.StackedInline):
    model = HousePlanPhoto
    max_num = 10
    extra = 0


class HouseFacadePhoto(models.Model):
    photo = models.FileField('Изображение фасада дома',
                             upload_to='house_facade_photos',
                             help_text='Изображение должно быть в формате avif, '
                                       'преобразовать можно '
                                       '<a href="https://imagetostl.com/ru/convert/file/jpg/to/avif" target="_blank">тут</a>',
                             validators=[FileExtensionValidator(['avif'])])
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    class Meta:
        verbose_name = "Изображение фасада проекта (дома)"
        verbose_name_plural = "Изображения фасадов проекта (дома)"

    def __str__(self):
        return self.house.name


class AdminHouseFacadePhoto(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: HouseFacadePhoto"""


class HouseFacadePhotoInlines(admin.StackedInline):
    model = HouseFacadePhoto
    max_num = 10
    extra = 0


class HousePhoto(models.Model):
    photo = models.FileField('Изображение',
                              upload_to='house_photos',
                              help_text='Изображение должно быть в формате avif, '
                                        'преобразовать можно '
                                        '<a href="https://imagetostl.com/ru/convert/file/jpg/to/avif" target="_blank">тут</a>',
                              validators=[FileExtensionValidator(['avif'])])
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    class Meta:
        verbose_name = "Дополнительная фотография дома"
        verbose_name_plural = "Дополнительные фотографии дома"

    def __str__(self):
        return self.house.name


class HousePhotoInlines(admin.StackedInline):
    model = HousePhoto
    max_num = 10
    extra = 0


class AdminHousePhoto(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: HousePhoto"""


class HouseType(models.Model):
    material = models.CharField('Материал стен', max_length=255)

    class Meta:
        verbose_name = "Тип дома"
        verbose_name_plural = "Типы домов"

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
    main_photo = models.FileField('Главное изображение',
                                   upload_to='house_main_photos',
                                   blank=True, null=True,
                                   help_text='Изображение должно быть в формате avif, '
                                             'преобразовать можно '
                                             '<a href="https://imagetostl.com/ru/convert/file/jpg/to/avif" target="_blank">тут</a>',
                                   validators=[FileExtensionValidator(['avif'])])
    cost_of_basic_equipment = models.CharField('Стоимость базовой комплектации', max_length=255, blank=True, null=True)
    building_materials_equipment = models.CharField("Стоимость стройматериалов", max_length=255, blank=True, null=True)
    link_to_video_on_youtube = models.CharField("Ссылка на видео в YouTub", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Проект дома"
        verbose_name_plural = "Проекты домов"

    def __str__(self):
        return self.name


class AdminHouse(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: House"""
    def photo(self, object):
        return mark_safe(f"<img src='{object.main_photo.url}' width=50>")

    inlines = [HousePhotoInlines, HousePlanPhotoInlines, HouseFacadePhotoInlines]
    list_display = ["name", "material", "photo", "cost_of_basic_equipment"]


class Contact(models.Model):
    address = models.CharField('Адрес', max_length=1000, blank=True, null=True)
    floor = models.CharField('Этаж', max_length=1000, blank=True, null=True)
    working_days = models.CharField("Рабочие дни", max_length=255, blank=True, null=True)
    working_hours = models.CharField('Время работы', max_length=500, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    phone_number = models.CharField('Номер телефона', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Наши контакты"
        verbose_name_plural = "Наши контакты"

    def __str__(self):
        return self.address


class AdminContact(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Contact"""
    list_display = ["address", "floor", "working_days", "working_hours", "email", "phone_number"]


class SocialMedia(models.Model):
    title_social_media = models.CharField('Социальная сеть', max_length=500)
    link = models.CharField("Ссылка", max_length=500, blank=True, null=True)
    phone_number = models.CharField('Номер телефона', max_length=255, blank=True, null=True)
    image = models.FileField('Иконка', upload_to='social_images')

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return self.title_social_media


class AdminSocialMedia(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: SocialMedia"""


class Partner(models.Model):
    title_partner = models.CharField('Имя партнера', max_length=500)
    image = models.ImageField('Изображение', upload_to='partner_images')

    class Meta:
        verbose_name = "Наш партнер"
        verbose_name_plural = "Наши партнеры"


    def __str__(self):
        return self.title_partner


class AdminPartner(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Partner"""


class Rating(models.Model):
    rating = models.CharField("Рейтинг", max_length=10)

    class Meta:
        verbose_name = "Рейтинг по отзывам на яндекс картах"
        verbose_name_plural = "Рейтинг по отзывам на яндекс картах"

    def __str__(self):
        return self.rating


class SignUpForAFreeConsultation(models.Model):
    name = models.CharField("Имя", max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255)
    date_of_consultation = models.DateField("Дата консультации")
    application_processed = models.BooleanField("Заявка обработана", default=False)

    class Meta:
        verbose_name = "Заявка на консультацию"
        verbose_name_plural = "Заявки на консультацию"

    def __str__(self):
        return f'{self.name}'


class AdminSignUpForAFreeConsultation(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: SignUpForAFreeConsultation"""
    list_display = ["name", "phone_number", "date_of_consultation", "application_processed"]
    list_editable = ["application_processed"]
    list_filter = ["application_processed", "date_of_consultation"]


class Fact(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    fact_description = models.CharField("Текст", max_length=500)

    class Meta:
        verbose_name = "Факт о нас"
        verbose_name_plural = "Факты о нас"

    def __str__(self):
        return self.title


class AdminFact(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Fact"""


class Vacancy(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    fact_description = models.CharField("Текст", max_length=500)
    is_publish = models.BooleanField("Опубликовано", default=False)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title


class AdminVacancy(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Vacancy"""
    list_display = ["title", "is_publish"]
    list_editable = ["is_publish"]
    list_filter = ["is_publish"]


class InfoCompany(models.Model):
    years_on_the_market = models.IntegerField("Лет на рынке недвижимости")
    satisfied_clients = models.IntegerField("Довольных клиентов")
    number_of_reviews = models.IntegerField("Количество отзывов")
    the_number_of_employees = models.IntegerField("Количество сотрудников")
    photo_ours_employer = models.FileField("Фото наших сотрудников",
                                           blank=True, null=True,
                                           help_text='Изображение должно быть в формате avif, '
                                                     'преобразовать можно '
                                                     '<a href="https://imagetostl.com/ru/convert/file/jpg/to/avif" target="_blank">тут</a>',
                                           validators=[FileExtensionValidator(['avif'])])

    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компании"

    def __str__(self):
        return "Информация о компании"


class AdminInfoCompany(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: InfoCompany"""
    list_display = ["id", "years_on_the_market", "satisfied_clients", "number_of_reviews", "the_number_of_employees"]


class CallBack(models.Model):
    name = models.CharField("Имя", max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255, blank=True, null=True)
    application_date = models.DateTimeField("Дата заявки", auto_now_add=True)
    application_processed = models.BooleanField("Заявка обработана", default=False)

    class Meta:
        verbose_name = "Заявка на обратный звонок"
        verbose_name_plural = "Заявки на обратный звонок"

    def __str__(self):
        return f'{self.name}'


class AdminCallBack(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: CallBack"""
    list_display = ["name", "phone_number", "application_date", "application_processed"]
    list_editable = ["application_processed"]
    list_filter = ["application_processed", "application_date"]


class BackgroundSliderImage(models.Model):
    image = models.FileField('Изображение', upload_to='background_images',
                             help_text='Изображение должно быть в формате avif, '
                                       'преобразовать можно '
                                       '<a href="https://imagetostl.com/ru/convert/file/jpg/to/avif" target="_blank">тут</a>',
                             validators=[FileExtensionValidator(['avif'])])

    class Meta:
        verbose_name = "Изображение в карусели банера сайта"
        verbose_name_plural = "Изображения в карусели банера сайта"

    def __str__(self):
        return f'{self.image}'


class AdminBackgroundSliderImage(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: BackgroundSliderImage"""
    def photo(self, object):
        return mark_safe(f"<img src='{object.image.url}' width=50>")
    list_display = ["image", "photo"]


class ImprovementPhoto(models.Model):
    photo = models.FileField('Изображение',
                             upload_to="improvement_photos",
                             help_text='Изображение должно быть в формате avif, '
                                       'преобразовать можно '
                                       '<a href="https://imagetostl.com/ru/convert/file/jpg/to/avif" target="_blank">тут</a>',
                             validators=[FileExtensionValidator(['avif'])])
    improvement = models.ForeignKey('Improvement', on_delete=models.CASCADE, verbose_name='Благоустройство')

    class Meta:
        verbose_name = "Дополнительное изображение благоустройства"
        verbose_name_plural = "Дополнительные изображения благоустройства"

    def __str__(self):
        return self.improvement.title


class AdminImprovementPhoto(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: ImprovementPhoto"""


class ImprovementPhotoInlines(admin.StackedInline):
    model = ImprovementPhoto
    max_num = 10
    extra = 0


class Improvement(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание")
    main_photo = models.FileField("Главное изображение",
                                  upload_to="improvement_main_photo",
                                  help_text='Изображение должно быть в формате avif, '
                                            'преобразовать можно '
                                            '<a href="https://imagetostl.com/ru/convert/file/jpg/to/avif" target="_blank">тут</a>',
                                  validators=[FileExtensionValidator(['avif'])])

    class Meta:
        verbose_name = "Вид работ по благоустройству"
        verbose_name_plural = "Виды работ по благоустройству"
    
    def __str__(self):
        return self.title


class AdminImprovement(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Improvement"""
    def photo(self, object):
        return mark_safe(f"<img src='{object.main_photo.url}' width=50>")

    inlines = [ImprovementPhotoInlines]
    list_display = ["title", "photo"]


class Review(models.Model):
    name = models.CharField("Имя человека оставившего отзыв", max_length=255)
    city_expert_level = models.CharField("Уровень знатока города", max_length=255)
    description = models.TextField("Текст отзыва")
    photo = models.FileField("Изображение",
                             upload_to="reviews_photo",
                             help_text='Изображение должно быть в формате avif, '
                                       'преобразовать можно '
                                       '<a href="https://imagetostl.com/ru/convert/file/jpg/to/avif" target="_blank">тут</a>',
                             validators=[FileExtensionValidator(['avif'])])
    is_publish = models.BooleanField("Опубликовано", default=False)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name


class AdminReview(admin.ModelAdmin):
    """Класс управления отображения
            в админ панели сущности: Review"""
    list_display = ["name", "is_publish"]
    list_editable = ["is_publish"]
    list_filter = ["is_publish"]

