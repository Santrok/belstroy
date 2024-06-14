# Generated by Django 5.0.6 on 2024-06-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundSliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='background_images', verbose_name='Изображение')),
            ],
        ),
        migrations.AlterField(
            model_name='house',
            name='main_photo',
            field=models.ImageField(blank=True, null=True, upload_to='house_main_photos', verbose_name='Главное изображение'),
        ),
        migrations.AlterField(
            model_name='housefacadephoto',
            name='photo',
            field=models.ImageField(upload_to='house_facade_photos', verbose_name='Изображение фасада дома'),
        ),
        migrations.AlterField(
            model_name='housephoto',
            name='photo',
            field=models.ImageField(upload_to='house_photos', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='houseplanphoto',
            name='photo',
            field=models.ImageField(upload_to='house_plan_photos', verbose_name='Изображение плана дома'),
        ),
        migrations.AlterField(
            model_name='housesectionphoto',
            name='photo',
            field=models.ImageField(upload_to='house_section_photos', verbose_name='Изображение дома в разрезе'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(upload_to='partner_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='image',
            field=models.FileField(upload_to='social_images', verbose_name='Иконка'),
        ),
    ]
