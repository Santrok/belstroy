import re

from rest_framework import serializers


def validate_phone(phone_number):
    # Валидация российского номера телефона
    if not re.match(r'^\+7\s?\(?\d{3}\)?\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}$', phone_number):
        raise serializers.ValidationError('Некорректный ввод номера телефона')