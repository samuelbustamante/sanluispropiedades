# -*- coding: utf-8 -*-

from django.db import models
from myproject.realestate.models import RealEstate
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

class Message(models.Model):
    send = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    realestate = models.ForeignKey(RealEstate)

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)
        self.send_email()

    def send_email(self):
        if not self.send:
            data = {
                'name': self.name,
                'phone': self.phone,
                'email': self.email,
                'message': self.message,
                'realestate': self.realestate
            }

            t_html = 'contact/message.html'
            t_text = 'contact/message.txt'

            html_content = render_to_string(t_html, data)
            text_content = render_to_string(t_text, data)

            to = 'SanLuisPropiedades <no-reply@sanluispropiedades.com>'
            subject = self.name + ' Desea contactarse con usted.'
        
            msg = EmailMultiAlternatives(subject, text_content, to,\
                  [self.realestate.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            # Averiguar como saber si se envio correctamente
            self.send = True
            self.save()
