from v1.models.errors import Service


def info(method):
    return Service.objects.filter(method=method).first().result()
