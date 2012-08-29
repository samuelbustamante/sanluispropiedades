# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

class RealEstateAdmin(admin.ModelAdmin):
    pass

admin.site.register(RealEstate, RealEstateAdmin)
