from django.db import models

categories = (
    ('BAJAJ','BAJAJ'),
    ('MOTO','MOTO'),
)

# Create your models here.
class Moto(models.Model):
	proprietaire = models.CharField(max_length=80,null=0,blank=0)
	Type = models.CharField(max_length=80,choices=categories)
	plaque = models.CharField(max_length=80,default="",null=0,blank=0)
	Numero_chasis = models.CharField(max_length=80,default="",null=0,blank=0)
	Adresse = models.CharField(max_length=80,default="",null=0,blank=0)
	CNI = models.CharField(max_length=80,default="",null=0,blank=0)
	Adresse = models.CharField(max_length=80,default="",null=0,blank=0)
	Telephone = models.CharField(max_length=80,default="",null=0,blank=0)