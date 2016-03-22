from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    contract = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    contact_mail = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def as_json(self):
	return dict(
	    id = self.id,
	    name = self.name,
	    contract = self.contract,
	    address = self.address,
	    contact_phone = self.contact_phone,
	    contact_mail = self.contact_mail,
	    description = self.description)

class People(models.Model):
    name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    contact_mail = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    employer = models.ForeignKey(Organisation)

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    nioss = models.CharField(max_length=100)
    contact =  models.ForeignKey(People)

class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.ForeignKey(Location)

class Port(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    device =  models.ForeignKey(Device)

