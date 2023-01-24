#  Unisoft Group Copyright (c) 2022/12/5
#
#  Created by Muzaffar Makhkamov
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from jsonrpcserver import Error, Success


def api_exception_handler():
    pass


def response_handler(response):
    print(f'Response Handler: {response}')
    if 'result' in response:
        return Success(response['result'])
    if 'error' in response:
        code = response['error']['code']
        message = response['error']['message']
        return Error(code, message)
    else:
        code = 999
        message = response
        if 'code' in response:
            code = response['code']
        if 'message' in response:
            message = response['message']

        return Error(code, message)
