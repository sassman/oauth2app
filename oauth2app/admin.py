# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)