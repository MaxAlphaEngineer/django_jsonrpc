#  Unisoft Group Copyright (c) 2022/12/5
#
#  Created by Muzaffar Makhkamov
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

import datetime
from re import compile as re_compile

import ujson as ujson
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from jsonrpcserver import method, Result, Success, dispatch

from api import settings
from v1.models.errors import Service
from v1.models.partners import AccessToken, User
from v1.services import service
from v1.utils.handlers import response_handler
from v1.utils.helpers import error_message
from v1.utils.validator import validator

# --------------------------- #
#       AUTHORIZATION
# --------------------------- #
AUTHORIZATION = ""


@method
def login(context, username: str, password: str) -> any:
    user = User.objects.filter(username=username)
    if user.exists():
        partner = user.first()
        if partner.check_password(password):
            tokens = AccessToken.objects.filter(partner=partner)
            if tokens.exists():
                return Success({
                    "access_token": tokens.first().key
                })
            token = AccessToken(partner=partner)
            token.generate()
            return Success({
                "access_token": token.key
            })
    else:
        return error_message(-32101, rpc_error=True)


# --------------------------- #
#       CARD
# --------------------------- #

CARD = ""


@method(name="service.info")
def service_info(context) -> Result:
    response = service.info(context['method_name'])
    return response_handler(response)


DISPATCH = ""


@csrf_exempt
def jsonrpc(request):
    # Json decode Error Handler
    try:
        body = ujson.loads(request.body)
    except ValueError:
        return error_message(-32700, rpc=True, json_response=True)

    request_id = body.get('id')
    headers = request.headers
    method_name = body['method']

    service = Service.objects.filter(method=method_name)
    if service.exists():
        if not service.first().is_active:
            return error_message(500, rpc=True, json_response=True)
    else:
        service = Service(method=method_name)
        service.save()

    # VALIDATE FIELDS
    validate = validator(body.get('params'))
    if 'error' in validate:
        return JsonResponse(validate, safe=False)

    context = {
        'request_id': request_id,
        'method_name': method_name
    }

    # Authorization
    if method_name not in settings.NO_LOGIN_METHODS:
        authorization = headers.get('Authorization', '')
        pattern = re_compile(r"Bearer (.+)")

        if not pattern.match(authorization):
            return error_message(-32102, rpc=True, json_response=True)

        input_token = pattern.findall(authorization)[0]

        # Authorize
        try:
            token = AccessToken.objects.get(key=input_token)
            context['user'] = token.partner
        except AccessToken.DoesNotExist:
            return error_message(-32103, rpc=True, json_response=True)

    # DISPATCH
    data = ujson.loads(dispatch(request.body.decode(), context=context))

    # RESPOND
    data['status'] = 'result' in data
    data['origin'] = method_name
    data['host'] = {
        'host': settings.APP_NAME,
        'timestamp': str(datetime.datetime.now())
    }

    return HttpResponse(ujson.dumps(data).encode(), content_type="application/json")
