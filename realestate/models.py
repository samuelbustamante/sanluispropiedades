# -*- coding: utf-8 -*-

from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User

class RealEstate(models.Model):
    user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=50, verbose_name=u'Nombre')
    address = models.CharField(max_length=50, verbose_name=u'Dirección')
    phone = models.CharField(max_length=30, verbose_name=u'Teléfono')
    email = models.EmailField(verbose_name=u'E-mail')
    logo = ImageWithThumbsField(upload_to='.', sizes=((101,84), (80,59)), verbose_name=u'Logo')
