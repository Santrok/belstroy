# Generated by Django 5.0.6 on 2024-06-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_improvement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя человека оставившего отзыв')),
                ('city_expert_level', models.CharField(max_length=255, verbose_name='Уровень знатока города')),
                ('description', models.TextField(verbose_name='Текст отзыва')),
                ('photo', models.ImageField(upload_to='reviews_photo', verbose_name='Изображение')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Опубликовано')),
            ],
        ),
    ]
