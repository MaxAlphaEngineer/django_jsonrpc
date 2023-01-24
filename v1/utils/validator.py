#  Unisoft Group Copyright (c) 2022/12/5
#
#  Created by Muzaffar Makhkamov
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from v1.utils.helpers import error_message

fields = [
    'username',
    'password',
    'ext_id',
    'number',
    'expire',
    'receiver',
    'phone',
    'date_from',
    'date_to',
    'person_code',
    'serial',
    'passport_id',
    'amount',
    'time',
    'merchant_id',
    'terminal_id',
    'type',
    'purpose'
]


def validator(params):
    for key, value in params.items():
        if key in fields:
            check = eval(f"{key}({repr(value)})")

            if check == True:
                print(key)
                continue
            else:
                return error_message(500, f'{key}-{value}')

    return {"result": True}


def username(value):
    if len(value) > 50 or len(value) < 4:
        return error_message(500)
    return True


def password(value):
    if len(value) > 50 or len(value) < 5:
        return error_message(500)
    return True


def ext_id(value):
    if len(value) > 50 or len(value) < 1:
        return error_message(500)
    return True


def number(value):
    if len(value) != 16:
        return error_message(32901)
    return True


def expire(value):
    if len(value) != 4:
        return error_message(32901)
    return True


def receiver(value):
    if len(value) != 16:
        return error_message(32901)
    return True


def phone(value):
    if len(value) != 12:
        return error_message(32901)
    return True


def date_from(value):
    if len(value) > 12 or len(value) < 6:
        return error_message(500)
    return True


def date_to(value):
    if len(value) > 12 or len(value) < 6:
        return error_message(500)
    return True


def person_code(value):
    if len(value) != 14:
        return error_message(32901)
    return True


def serial(value):
    if len(value) != 2:
        return error_message(32901)
    return True


def passport_id(value):
    if len(value) != 7:
        return error_message(32901)
    return True


def amount(value):
    if value < 1_000 or value > 10_000_000:
        return error_message(32901)
    return True


def time(value):
    if value < 1 or value > 1_440:
        return error_message(32901)
    return True


def merchant_id(value):
    if len(value) > 15 or len(value) < 14:
        return error_message(32901)
    return True


def terminal_id(value):
    if len(value) > 10 or len(value) < 6:
        return error_message(32901)
    return True


def type(value):
    if value not in [1, 2, 3]:
        return error_message(32901)
    return True


def purpose(value):
    if len(value) > 30 or len(value) < 6:
        return error_message(32901)
    return True
