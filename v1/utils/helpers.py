#  Unisoft Group Copyright (c) 2022/12/5
#
#  Created by Muzaffar Makhkamov
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

import datetime

from django.http import JsonResponse

from api import settings
from v1.models import Error


def phone_mask(number):
    return number


def card_mask(number):
    return number


def error_message(code, message=None, origin="", request_id=None, wrapper=False, rpc=False, json_response=False,
                  rpc_error=False):
    error = Error.objects.filter(code=code)
    if error.exists():
        error = error.first()
        message = {
            "uz": error.uz,
            "ru": error.ru,
            "en": error.en
        }
        data = {
            "code": error.code,
            "message": message
        }
    else:
        if message is None:
            message = {
                "uz": "Nomalum xatolik yuz berdi",
                "ru": "Произошла неопределенная ошибка",
                "en": "Undefined error occurred",
            }
            data = {
                "code": code,
                "message": message
            }
        else:
            data = {
                "code": code,
                "message": message
            }

    if wrapper:
        data = {"error": data}

    if rpc:
        data = {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": data,
            "status": False,
            "origin": origin,
            "host": {
                "host": settings.APP_NAME,
                "timestamp": str(datetime.datetime.now())
            }
        }

    if json_response:
        data = JsonResponse(data, safe=False)

    if rpc_error:
        from jsonrpcserver import Error as RpcError
        return RpcError(code, message)

    return data


def url_action_helper(service, test=False):
    pass
