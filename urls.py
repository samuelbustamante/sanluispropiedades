# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^test', include('myproject.properties.urls')),
    url(r'^test/administrador/', include(admin.site.urls)),
    url(r'^test/contacto/', include('myproject.contact.urls')),
    url(r'^', direct_to_template, {'template': 'fleepy.html'}),
)

