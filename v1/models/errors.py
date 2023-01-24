#  Unisoft Group Copyright (c) 2022/12/5
#
#  Created by Muzaffar Makhkamov
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.db import models

from api import settings


class Error(models.Model):
    # code
    code = models.IntegerField('Error code')
    alias = models.IntegerField('Alias Code from origin', null=True)
    origin = models.CharField('Origin', max_length=50, default=settings.APP_NAME)
    en = models.CharField("English", max_length=60)
    uz = models.CharField("O'zbekcha", max_length=60, null=True)
    ru = models.CharField("Русский", max_length=60, null=True)

    class Meta:
        verbose_name_plural = "6. Errors"

    pass


class Service(models.Model):
    method = models.CharField("Method Name", max_length=60)
    is_active = models.BooleanField(default=True)
    is_test = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "7. Services"

    def result(self):
        return {
            "result": {
                "method": self.method,
                "is_test": self.is_test,
                "is_active": self.is_active
            }

        }
