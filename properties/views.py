# -*- coding: utf-8 -*-

from models import Departament, House, Office, LocalBusiness, Shed, Land
from django.shortcuts import render_to_response
from django.views.generic import list_detail
from django.template import RequestContext


#----- Departament -----#

def departament_sale_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=Departament.sale.all(),
        template_name='properties/departament_sale_detail.html',
    )

def departament_rent_detail(request, object_id):
    return list_detail.object_detail( 
        request,
        object_id=object_id,
        queryset=Departament.rent.all(),
        template_name='properties/departament_rent_detail.html',
    )

def departament_sale_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset=Departament.sale.all(),
        template_name='properties/departament_sale_list.html',
        paginate_by=20,
        page=page
    )

def departament_rent_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset=Departament.rent.all(),
        template_name='properties/departament_rent_list.html',
        paginate_by=20,
        page=page
    )

#-------- House --------#

def house_sale_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=House.sale.all(),
        template_name='properties/house_sale_detail.html',
    )

def house_rent_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=House.rent.all(),
        template_name='properties/house_rent_detail.html',
    )

def house_sale_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset = House.sale.all(),
        template_name='properties/house_sale_list.html',
        paginate_by=20,
        page=page
    )

def house_rent_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset = House.rent.all(),
        template_name='properties/house_rent_list.html',
        paginate_by=20,
        page=page
    )

#------- Office -------#

def office_sale_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=Office.sale.all(),
        template_name='properties/office_sale_detail.html',
    )

def office_rent_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=Office.rent.all(),
        template_name='properties/office_rent_detail.html',
    )

def office_sale_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset = Office.sale.all(),
        template_name='properties/office_sale_list.html',
        paginate_by=20,
        page=page
    )

def office_rent_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset = Office.rent.all(),
        template_name='properties/office_rent_list.html',
        paginate_by=20,
        page=page
    )

#--- Local Business ---#

def localbusiness_sale_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=LocalBusiness.sale.all(),
        template_name='properties/localbusiness_sale_detail.html',
    )

def localbusiness_rent_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=LocalBusiness.rent.all(),
        template_name='properties/localbusiness_rent_detail.html',
    )

def localbusiness_sale_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset = LocalBusiness.sale.all(),
        template_name='properties/localbusiness_sale_list.html',
        paginate_by=20,
        page=page
    )

def localbusiness_rent_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset = LocalBusiness.rent.all(),
        template_name='properties/localbusiness_rent_list.html',
        paginate_by=20,
        page=page
    )

#-------- Shed --------#

def shed_sale_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=Shed.sale.all(),
        template_name='properties/shed_sale_detail.html',
    )

def shed_rent_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=Shed.rent.all(),
        template_name='properties/shed_rent_detail.html',
    )

def shed_sale_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset = Shed.sale.all(),
        template_name='properties/shed_sale_list.html',
        paginate_by=20,
        page=page
    )

def shed_rent_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset = Shed.rent.all(),
        template_name='properties/shed_rent_list.html',
        paginate_by=20,
        page=page
    )

#-------- Land --------#

def land_sale_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=Land.sale.all(),
        template_name='properties/land_sale_detail.html',
    )

def land_rent_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=Land.rent.all(),
        template_name='properties/land_rent_detail.html',
    )

def land_sale_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset = Land.sale.all(),
        template_name='properties/land_sale_list.html',
        paginate_by=20,
        page=page
    )

def land_rent_list(request, page=1):
    return list_detail.object_list(
        request,
        queryset = Land.sale.all(),
        template_name='properties/land_rent_list.html',
        paginate_by=20,
        page=page
    )

#-------- Search --------#

#def simple_search(request):
#    if request.method == 'POST':
#        form = VehicleForm(request.POST, request.FILES)
#        if form.is_valid():
#            model = form.save(commit=False)
#            model.user = request.user
#            model.save()
#            return render_to_response('vehicles/success.html', locals(),\
#                context_instance=RequestContext(request))
#    else:
#        form = VehicleForm()
#    return render_to_response('vehicles/vehicle_form.html', locals(),\
#        context_instance=RequestContext(request))
