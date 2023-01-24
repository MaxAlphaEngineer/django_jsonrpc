#  Unisoft Group Copyright (c) 2022/12/5
#
#  Created by Muzaffar Makhkamov
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.core.management.base import BaseCommand

from v1.models import Error


class Command(BaseCommand):
    help = 'Populates error codes after migration'

    # def add_arguments(self, parser):
    #     parser.add_argument('error_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for error_item in self.errors:
            # if error code exists do nothing
            error = Error.objects.filter(code=error_item['code'])
            if error.exists():
                self.stdout.write(self.style.WARNING(f'Exist:'))
                print(error_item["code"])
            # else create error
            else:
                Error(code=error_item['code'], origin=error_item['origin'], uz=error_item['uz'], ru=error_item['ru'],
                      en=error_item['en'], ).save()

                self.stdout.write(self.style.SUCCESS(f'Created:'))
                print(error_item["code"])
        self.stdout.write(self.style.SUCCESS('Command finished'))

    errors = [
        # Validators
        {
            "code": 500,
            "origin": "service",
            "uz": "Servis vaqtinchalik mavjud emas!",
            "ru": "Сервис временно недоступен!",
            "en": "Service is temporarily unavailable!"
        },

        {
            "code": -32700,
            "origin": "parse",
            "uz": "So\'rov noto\'g\'ri jo\'natilgan",
            "ru": "Тело запроса неверно",
            "en": "Request body incorrect"
        },

        # AUTHORIZATION
        {
            "code": -32101,
            "origin": "authorization",
            "uz": "Foydalanuvchi nomi yoki parol noto\'g\'ri",
            "ru": "Имя пользователя или пароль неверен",
            "en": "Username or password incorrect"
        },
        {
            "code": -32102,
            "origin": "authorization",
            "uz": "Avtorizatsiya qilish uchun  headerda \'token\' dan foydalaning",
            "ru": "Используйте \'token\' в  header.",
            "en": "Use token in your headers with given for you \'token\' to authorize"
        },
        {
            "code": -32103,
            "origin": "authorization",
            "uz": "Avtorizatsiya tokeni muddati tugagan yoki yaroqsiz",
            "ru": "Срок действия токена авторизации истек или недействителен",
            "en": "Authorization token expired or not valid"
        },


        # CHEQUE
        {
            "code": -32401,
            "origin": "cheque",
            "uz": "External ID oldin foydalanilgan!",
            "ru": "External ID уже существует!",
            "en": "External ID already exists!"
        },

        {
            "code": -32402,
            "origin": "cheque",
            "uz": "External ID topilmadi!",
            "ru": "External ID не найден!",
            "en": "External ID not found!"
        },

    ]
