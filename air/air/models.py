#demo/api/models.py
from django.db import models


class Air(models.Model):
    #If you want to set an id, declare AutoField(primary_key=True).
	airCode =  models.CharField(max_length=100)
	airCna =  models.CharField(max_length=100)
	status =  models.CharField(max_length=100)
	reserve1 =  models.CharField(max_length=100)
	reserve2 =  models.CharField(max_length=100)
	reserve3 =  models.CharField(max_length=100)
	reserve4 =  models.CharField(max_length=100)
	reserve5 =  models.CharField(max_length=100)
	airC =  models.CharField(max_length=100)
	airF =  models.CharField(max_length=100)
	airFna =  models.CharField(max_length=100)
	airTotal =  models.CharField(max_length=100)
	airY =  models.CharField(max_length=100)
	airYna =  models.CharField(max_length=100)
	class Meta:
		db_table = 'air'
		verbose_name = "Air"
		verbose_name_plural = verbose_name
	def __str__(self):
		return ""