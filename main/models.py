from django.db import models

# Create your models here.


class HousePlanPhoto(models.Model):
    photo = models.ImageField('Изображение плана дома')
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    def __str__(self):
        return self.house.name


class HouseFacadePhoto(models.Model):
    photo = models.ImageField('Изображение фасада дома')
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    def __str__(self):
        return self.house.name


class HouseSectionPhoto(models.Model):
    photo = models.ImageField('Изображение дома в разрезе')
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    def __str__(self):
        return self.house.name


class HousePhoto(models.Model):
    photo = models.ImageField('Изображение')
    house = models.ForeignKey('House', on_delete=models.CASCADE, verbose_name='Дом')

    def __str__(self):
        return self.house.name


class HouseType(models.Model):
    material = models.CharField('Материал стен', max_length=255)

    def __str__(self):
        return self.material


class House(models.Model):
    name = models.CharField('Название дома', max_length=500)
    facade = models.CharField('Фасад', max_length=500)
    square = models.CharField('Площадь', max_length=500)
    room = models.CharField('Количество комнат', max_length=500)
    bathroom = models.CharField('Количество санузлов', max_length=500)
    floor = models.CharField('Количество этажей', max_length=500)
    description = models.TextField('Описание дома')
    material = models.ForeignKey('HouseType', on_delete=models.CASCADE, verbose_name='Материал стен')
    main_photo = models.ImageField('Главное изображение')
    cost_of_basic_equipment = models.CharField('Стоимость базовой комплектации', max_length=255)


    def __str__(self):
        return self.name


class TypeOfWork(models.Model):
    title_of_work = models.CharField('Тип работ', max_length=1000)

    def __str__(self):
        return self.title_of_work


class Subwork(models.Model):
    title_of_subwork = models.CharField('Вид работы', max_length=1000)
    price = models.DecimalField('Стоимость работы', max_digits=14, decimal_places=2)

    def __str__(self):
        return self.title_of_subwork


class Contact(models.Model):
    address = models.CharField('Адрес', max_length=1000)
    floor = models.CharField('Этаж', max_length=1000)
    working_hours = models.CharField('Время работы', max_length=500)
    email = models.EmailField('Email')
    phone_number = models.CharField('Номер телефона', max_length=500)


class SocialMedia(models.Model):
    title_social_media = models.CharField('Социальная сеть', max_length=500)
    phone_number = models.CharField('Номер телефона', max_length=255)
    image = models.ImageField('Иконка')

    def __str__(self):
        return self.title_social_media


class Partner(models.Model):
    title_partner = models.CharField('Имя партнера', max_length=500)
    image = models.ImageField('Изображение')

    def __str__(self):
        return self.title_partner

