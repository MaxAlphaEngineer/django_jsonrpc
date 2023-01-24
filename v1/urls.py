from django.urls import path

from v1.views import jsonrpc

urlpatterns = [
    path('jsonrpc', jsonrpc)
]
