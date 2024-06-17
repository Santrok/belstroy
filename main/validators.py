import re

from rest_framework import serializers


def validate_phone(phone_number):
    # Валидация российского номера телефона
    if not re.match(r'^(\d{1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})', phone_number):
        raise serializers.ValidationError('Некорректный ввод номера телефона')