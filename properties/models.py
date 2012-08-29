# -*- coding: utf-8 -*-

from choices import *
from django.db import models
from thumbs import ImageWithThumbsField
from myproject.realestate.models import RealEstate

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.name

class SaleManager(models.Manager):
    def get_query_set(self):
        return super(SaleManager, self).get_query_set().filter(operation='s')

class RentManager(models.Manager):
    def get_query_set(self):
        return super(RentManager, self).get_query_set().filter(operation='r')

class Property(models.Model):
    propietor = models.ForeignKey(RealEstate)
    operation = models.CharField(max_length=1, choices=OPERATIONS, verbose_name=u'Operación')
    price = models.PositiveIntegerField(verbose_name=u'Precio en Pesos')
    location = models.CharField(max_length=2, choices=LOCATIONS, verbose_name=u'Localidad')
    address = models.CharField(max_length=100, verbose_name=u'Dirección')
    orientation = models.CharField(max_length=1, choices=ORIENTATIONS, verbose_name=u'Orientación')
    services = models.ManyToManyField(Service, verbose_name=u'Servicios')
    description = models.TextField(verbose_name=u'Descripción')
    image0 = ImageWithThumbsField(upload_to='.', sizes=((45,33),(131,85),(485,300)), verbose_name=u'Imagen 1')
    image1 = ImageWithThumbsField(upload_to='.', sizes=((45,33),(131,85),(485,300)), blank=True, verbose_name=u'Imagen 2')
    image2 = ImageWithThumbsField(upload_to='.', sizes=((45,33),(131,85),(485,300)), blank=True, verbose_name=u'Imagen 3')
    image3 = ImageWithThumbsField(upload_to='.', sizes=((45,33),(131,85),(485,300)), blank=True, verbose_name=u'Imagen 4')
    image4 = ImageWithThumbsField(upload_to='.', sizes=((45,33),(131,85),(485,300)), blank=True, verbose_name=u'Imagen 5')
    image5 = ImageWithThumbsField(upload_to='.', sizes=((45,33),(131,85),(485,300)), blank=True, verbose_name=u'Imagen 6')
    image6 = ImageWithThumbsField(upload_to='.', sizes=((45,33),(131,85),(485,300)), blank=True, verbose_name=u'Imagen 7')
    image7 = ImageWithThumbsField(upload_to='.', sizes=((45,33),(131,85),(485,300)), blank=True, verbose_name=u'Imagen 8')
    image8 = ImageWithThumbsField(upload_to='.', sizes=((45,33),(131,85),(485,300)), blank=True, verbose_name=u'Imagen 9')
    image9 = ImageWithThumbsField(upload_to='.', sizes=((45,33),(131,85),(485,300)), blank=True, verbose_name=u'Imagen 10')
    latitude = models.CharField(max_length='20')
    longitude = models.CharField(max_length='20')
    sale = SaleManager()
    rent = RentManager()

    def get_number_images(self):
        counter = 1
        if self.image1: counter += 1
        if self.image2: counter += 1
        if self.image3: counter += 1
        if self.image4: counter += 1
        if self.image5: counter += 1
        if self.image6: counter += 1
        if self.image7: counter += 1
        if self.image8: counter += 1
        if self.image9: counter += 1
        return counter

    class Meta:
        abstract = True
        ordering = ('-id',)

class Departament(Property):
    ambiences = models.PositiveIntegerField(default=0, verbose_name=u'Ambientes')
    rooms = models.PositiveIntegerField(default=0, verbose_name=u'Habitaciones')
    state = models.CharField(max_length=1, choices=STATES, verbose_name=u'Estado')
    baths = models.PositiveIntegerField(default=0, verbose_name=u'Baños')
    old = models.CharField(max_length=1, choices=OLDS, verbose_name=u'Antigüedad')
    surfaces = models.PositiveIntegerField(default=0, verbose_name=u'Superficie Total')
    surfaces_coated = models.PositiveIntegerField(default=0, verbose_name=u'Superficie cubierta')
    garages = models.PositiveIntegerField(default=0, verbose_name=u'Garages')
    garages_coated = models.PositiveIntegerField(default=0, verbose_name=u'Garages Cubiertos')
    lifts = models.PositiveIntegerField(default=0, verbose_name=u'Ascensores')
    luminosity = models.CharField(max_length=1, choices=LUMINOSITY, verbose_name=u'Luminosidad')
    professional = models.BooleanField(verbose_name=u'Apto Profesional')
    commercial = models.BooleanField(verbose_name=u'Apto Comercial')
    expences = models.PositiveIntegerField(default=0, verbose_name=u'Expensas')

    class Meta:
        verbose_name = u'Departamento'
        verbose_name_plural = u'Departamentos'

class House(Property):
    ambiences = models.PositiveIntegerField(default=0, verbose_name=u'Ambientes')
    rooms = models.PositiveIntegerField(default=0, verbose_name=u'Habitaciones')
    state = models.CharField(max_length=1, choices=STATES, verbose_name=u'Estado')
    baths = models.PositiveIntegerField(default=1, verbose_name=u'Baños')
    old = models.CharField(max_length=1, choices=OLDS, verbose_name=u'Antigüedad')
    surfaces = models.PositiveIntegerField(default=0, verbose_name=u'Superficie Total')
    surfaces_coated = models.PositiveIntegerField(default=0, verbose_name=u'Superficie Cubierta')
    garages = models.PositiveIntegerField(default=0, verbose_name=u'Garages')
    garages_coated = models.PositiveIntegerField(default=0, verbose_name=u'Garages Cubiertos')
    floors = models.PositiveIntegerField(default=1, verbose_name=u'Plantas')
    luminosity = models.CharField(max_length=1, choices=LUMINOSITY, verbose_name=u'Luminosidad')
    professional = models.BooleanField(verbose_name=u'Apto profesional')
    commercial = models.BooleanField(verbose_name=u'Apto Comercial')

    class Meta:
        verbose_name = u'Casa'
        verbose_name_plural = u'Casas'

class Office(Property):
    ambiences = models.PositiveIntegerField(default=0, verbose_name=u'Ambientes')
    rooms = models.PositiveIntegerField(default=0, verbose_name=u'Habitaciones')
    expenses = models.PositiveIntegerField(default=0, verbose_name=u'Expensas en pesos')
    state = models.CharField(max_length=1, choices=STATES, verbose_name=u'Estado')
    baths = models.PositiveIntegerField(default=0, verbose_name=u'Baños')
    old = models.CharField(max_length=1, choices=OLDS, verbose_name=u'Antigüedad')
    surfaces = models.PositiveIntegerField(default=0, verbose_name=u'Superficie Total')
    surfaces_coated = models.PositiveIntegerField(default=0, verbose_name=u'Superficie Cubierta')
    garages = models.PositiveIntegerField(default=0, verbose_name=u'Garages')
    garages_coated = models.PositiveIntegerField(default=0, verbose_name=u'Garages Cubiertos')
    lifts = models.PositiveIntegerField(default=0, verbose_name=u'Ascensores')
    floor = models.PositiveIntegerField(default=1, verbose_name=u'Planta')
    luminosity = models.CharField(max_length=1, choices=LUMINOSITY, verbose_name=u'Luminosidad')
    professional = models.BooleanField(verbose_name=u'Apto Profesional')
    commercial = models.BooleanField(verbose_name=u'Apto Comercial')

    class Meta:
        verbose_name = u'Oficina'
        verbose_name_plural = u'Oficinas'

class LocalBusiness(Property):
    state = models.CharField(max_length=1, choices=STATES, verbose_name=u'Estado')
    baths = models.PositiveIntegerField(default=1, verbose_name=u'Baños')
    old = models.CharField(max_length=1, choices=OLDS, verbose_name=u'Antigüedad')
    surfaces = models.PositiveIntegerField(default=0, verbose_name=u'Superficie Total')
    surfaces_coated = models.PositiveIntegerField(default=0, verbose_name=u'Superficie Cubierta')
    garages = models.PositiveIntegerField(default=0, verbose_name=u'Garages')
    garages_coated = models.PositiveIntegerField(default=0, verbose_name=u'Garages Cubiertos')
    luminosity = models.CharField(max_length=1, choices=LUMINOSITY, verbose_name=u'Luminosidad')

    class Meta:
        verbose_name = u'Local Comercial'
        verbose_name_plural = u'Locales Comerciales'

class Shed(Property):
    state = models.CharField(max_length=1, choices=STATES, verbose_name=u'Estado')
    baths = models.PositiveIntegerField(default=1, verbose_name=u'Baños')
    old = models.CharField(max_length=1, choices=OLDS, verbose_name=u'Antigüedad')
    surfaces = models.PositiveIntegerField(default=0, verbose_name=u'Superficie Total')
    surfaces_coated = models.PositiveIntegerField(default=0, verbose_name=u'Superficie Cubierta')
    garages = models.PositiveIntegerField(default=0, verbose_name=u'Garages')
    garages_coated = models.PositiveIntegerField(default=0, verbose_name=u'Garages Cubiertos')
    commercial = models.BooleanField(verbose_name=u'Apto Comercial')

    class Meta:
        verbose_name = u'Galpón'
        verbose_name_plural = u'Galpones'

class Land(Property):
    type_land = models.CharField(max_length=1, choices=TYPES_LAND, verbose_name=u'Tipo')
    pavement = models.CharField(max_length=10, verbose_name=u'Distancia a Pavimento')
    fencing = models.BooleanField(verbose_name=u'Cercado ?')
    livestock = models.BooleanField(verbose_name=u'Apto para Ganado ?')
    agriculture = models.BooleanField(verbose_name=u'Apto para Agricultura ?')
    pricipal_home = models.BooleanField(verbose_name=u'Posee Casa Principal ?')
    secundary_house = models.BooleanField(verbose_name=u'Posee Casa Secundaria ?')
    occupied = models.BooleanField(verbose_name=u'Ocupada')
    length_front = models.IntegerField(verbose_name=u'Longitud de Frente')
    length_back = models.IntegerField(verbose_name=u'Longitud de Fondo')
    total_surface = models.IntegerField(verbose_name=u'Superficie Total')
    contructed_surface = models.IntegerField(verbose_name=u'Superficie Construida')
    free_surface = models.IntegerField(verbose_name=u'Superfie Libre')
    form = models.CharField(max_length=1, choices=FORMS, verbose_name=u'Forma')
    topographic_level = models.CharField(max_length=1, choices=TOPOGRAFICS, verbose_name=u'Tipografía')

    class Meta:
        verbose_name = u'Terreno'
        verbose_name_plural = u'Terrenos'
