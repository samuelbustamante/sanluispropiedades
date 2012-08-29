# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url, include
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',

    url(r'^/$', direct_to_template, {'template': 'index.html'}, name='index'),

    #----- Departament ----#

    url(r'^departamento/venta/(?P<object_id>\d+)/([-\w]+)/$',
        departament_sale_detail, name='departament_sale_detail'
    ),
    url(r'^departamento/alquiler/(?P<object_id>\d+)/([-\w]+)/$',
        departament_rent_detail, name='departament_rent_detail'
    ),
    url(r'^departamentos/venta/$',
        departament_sale_list, name='departament_sale_list'
    ),
    url(r'^departamentos/alquiler/$',
        departament_rent_list, name='departament_rent_list'
    ),

    #-------- House -------#

    url(r'^casa/venta/(?P<object_id>\d+)/([-\w]+)/$',
        house_sale_detail, name='house_sale_detail'
    ),
    url(r'^casa/alquiler/(?P<object_id>\d+)/([-\w]+)/$',
        house_rent_detail, name='house_rent_detail'
    ),
    url(r'^casas/venta/$',
        house_sale_list, name='house_sale_list'
    ),
    url(r'^casas/alquiler/$',
        house_rent_list, name='house_rent_list'
    ),

    #------- Office -------#

    url(r'^oficina/venta/(?P<object_id>\d+)/([-\w]+)/$',
        office_sale_detail, name='office_sale_detail'
    ),
    url(r'^oficina/alquiler/(?P<object_id>\d+)/([-\w]+)/$',
        office_rent_detail, name='office_rent_detail'
    ),
    url(r'^oficinas/venta/$',
        office_sale_list, name='office_sale_list'
    ),
    url(r'^oficinas/alquiler/$',
        office_rent_list, name='office_rent_list'
    ),

    #--- Local Business ---#

    url(r'^local-comercial/venta/(?P<object_id>\d+)/([-\w]+)/$',
        localbusiness_sale_detail, name='localbusiness_sale_detail'
    ),
    url(r'^local-comercial/alquiler/(?P<object_id>\d+)/([-\w]+)/$',
        localbusiness_rent_detail, name='localbusiness_rent_detail'
    ),
    url(r'^locales-comerciales/venta/$',
        localbusiness_sale_list, name='localbusiness_sale_list'
    ),
    url(r'^locales-comerciales/alquiler/$',
        localbusiness_rent_list, name='localbusiness_rent_list'
    ),

    #-------- Shed --------#

    url(r'^galpon/venta/(?P<object_id>\d+)/([-\w]+)/$',
        shed_sale_detail, name='shed_sale_detail'
    ),
    url(r'^galpon/alquiler/(?P<object_id>\d+)/([-\w]+)/$',
        shed_rent_detail, name='shed_rent_detail'
    ),
    url(r'^galpones/venta/$',
        shed_sale_list, name='shed_sale_list'
    ),
    url(r'^galpones/alquiler/$',
        shed_rent_list, name='shed_rent_list'
    ),

    #-------- Land --------#

    url(r'^terreno/venta/(?P<object_id>\d+)/([-\w]+)/$',
        land_sale_detail, name='land_sale_detail'
    ),
    url(r'^terreno/alquiler/(?P<object_id>\d+)/([-\w]+)/$',
        land_rent_detail, name='land_rent_detail'
    ),
    url(r'^terrenos/venta/$',
        land_sale_list, name='land_sale_list'
    ),
    url(r'^terrenos/alquiler/$',
        land_rent_list, name='land_rent_list'
    ),
)
