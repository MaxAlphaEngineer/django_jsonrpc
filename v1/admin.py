#  Unisoft Group Copyright (c) 2022/12/5
#
#  Created by Muzaffar Makhkamov
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from v1.models import Error
from v1.models.errors import Service
from v1.models.partners import Partner


# Register your models here.
@admin.register(Partner)
class PartnerAdmin(UserAdmin):
    list_display = 'id', 'username', 'is_active', 'is_superuser'
    list_display_links = 'id', 'username'
    list_editable = []
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        # (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_test",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )


@admin.register(Error)
class ErrorAdminModel(admin.ModelAdmin):
    list_display = [field.name for field in Error._meta.fields]


@admin.register(Service)
class ServiceAdminModel(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]
