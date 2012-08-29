# -*- coding: utf-8 -*-

from myproject.realestate.models import RealEstate
from django.contrib import admin
from models import *

class ServiceAdmin(admin.ModelAdmin):
    pass

class DepartamentAdmin(admin.ModelAdmin):
    #fields = (
    #    'operation', 'price',
    #    ('location', 'address'),
    #    'orientation', 'services',
    #    'description',
    #    ('image0', 'image1'), ('image2', 'image3'), ('image4', 'image5'), ('image6', 'image7'), ('image8', 'image9')
    #)
    exclude = ('propietor',)
    list_display = ('address', 'price', 'ambiences', 'rooms', 'operation', 'location', 'professional', 'commercial')
    list_filter = ('operation', 'location')

    def queryset(self, request):
        qs = super(DepartamentAdmin, self).queryset(request)
        return qs.filter(propietor=RealEstate.objects.get(user=request.user))

    def save_model(self, request, obj, form, change):
        obj.propietor = RealEstate.objects.get(user=request.user)
        obj.save()

    class Media:
        js = (
          'http://maps.google.com/maps/api/js?sensor=false',
          '/static/js/jquery-1.4.4.min.js',
          '/static/js/jquery-ui-1.8.7.min.js',
          '/static/js/jquery.ui.addresspicker.js',
          '/static/js/map_admin.js'
        )

class HouseAdmin(admin.ModelAdmin):
    exclude = ('propietor',)
    list_display = ('address', 'price', 'ambiences', 'rooms', 'operation', 'location', 'professional', 'commercial')
    list_filter = ('operation', 'location')

    def queryset(self, request):
        qs = super(HouseAdmin, self).queryset(request)
        return qs.filter(propietor=RealEstate.objects.get(user=request.user))

    def save_model(self, request, obj, form, change):
        obj.propietor = RealEstate.objects.get(user=request.user)
        obj.save()

    class Media:
        js = (
          'http://maps.google.com/maps/api/js?sensor=false',
          '/static/js/jquery-1.4.4.min.js',
          '/static/js/jquery-ui-1.8.7.min.js',
          '/static/js/jquery.ui.addresspicker.js',
          '/static/js/map_admin.js'
        )

class OfficeAdmin(admin.ModelAdmin):
    exclude = ('propietor',)
    list_display = ('address', 'price', 'ambiences', 'rooms', 'operation', 'location', 'professional', 'commercial')
    list_filter = ('operation', 'location')

    def queryset(self, request):
        qs = super(OfficeAdmin, self).queryset(request)
        return qs.filter(propietor=RealEstate.objects.get(user=request.user))

    def save_model(self, request, obj, form, change):
        obj.propietor = RealEstate.objects.get(user=request.user)
        obj.save()

    class Media:
        js = (
          'http://maps.google.com/maps/api/js?sensor=false',
          '/static/js/jquery-1.4.4.min.js',
          '/static/js/jquery-ui-1.8.7.min.js',
          '/static/js/jquery.ui.addresspicker.js',
          '/static/js/map_admin.js'
        )

class LocalBusinessAdmin(admin.ModelAdmin):
    exclude = ('propietor',)
    list_display = ('address', 'price', 'operation', 'location')
    list_filter = ('operation', 'location')

    def queryset(self, request):
        qs = super(LocalBusinessAdmin, self).queryset(request)
        return qs.filter(propietor=RealEstate.objects.get(user=request.user))

    def save_model(self, request, obj, form, change):
        obj.propietor = RealEstate.objects.get(user=request.user)
        obj.save()

    class Media:
        js = (
          'http://maps.google.com/maps/api/js?sensor=false',
          '/static/js/jquery-1.4.4.min.js',
          '/static/js/jquery-ui-1.8.7.min.js',
          '/static/js/jquery.ui.addresspicker.js',
          '/static/js/map_admin.js'
        )

class ShedAdmin(admin.ModelAdmin):
    exclude = ('propietor',)
    list_display = ('address', 'price', 'operation', 'location')
    list_filter = ('operation', 'location')

    def queryset(self, request):
        qs = super(ShedAdmin, self).queryset(request)
        return qs.filter(propietor=RealEstate.objects.get(user=request.user))

    def save_model(self, request, obj, form, change):
        obj.propietor = RealEstate.objects.get(user=request.user)
        obj.save()

    class Media:
        js = (
          'http://maps.google.com/maps/api/js?sensor=false',
          '/static/js/jquery-1.4.4.min.js',
          '/static/js/jquery-ui-1.8.7.min.js',
          '/static/js/jquery.ui.addresspicker.js',
          '/static/js/map_admin.js'
        )

class LandAdmin(admin.ModelAdmin):
    exclude = ('propietor',)
    list_display = ('address', 'price', 'type_land', 'operation', 'location')
    list_filter = ('operation', 'type_land', 'location')

    def queryset(self, request):
        qs = super(LandAdmin, self).queryset(request)
        return qs.filter(propietor=RealEstate.objects.get(user=request.user))

    def save_model(self, request, obj, form, change):
        obj.propietor = RealEstate.objects.get(user=request.user)
        obj.save()

    class Media:
        js = (
          'http://maps.google.com/maps/api/js?sensor=false',
          '/static/js/jquery-1.4.4.min.js',
          '/static/js/jquery-ui-1.8.7.min.js',
          '/static/js/jquery.ui.addresspicker.js',
          '/static/js/map_admin.js'
        )

admin.site.register(Service, ServiceAdmin)
admin.site.register(Departament, DepartamentAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(LocalBusiness, LocalBusinessAdmin)
admin.site.register(Shed, ShedAdmin)
admin.site.register(Land, LandAdmin)
