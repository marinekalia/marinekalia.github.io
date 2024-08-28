# home/models.py
from django.db import models

class Hospital(models.Model):
	hopital_id = models.CharField(max_length=100, unique=True)

	def __str__(self):
	    return self.hopital_id

class HospitalName(models.Model):
	name = models.CharField(max_length=255, unique=True)

	def __str__(self):
    	    return self.name
