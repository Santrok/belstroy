# Generated by Django 5.0.6 on 2024-06-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_socialmedia_link_alter_socialmedia_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='link_to_video_on_youtube',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на видео в YouTub'),
        ),
    ]
