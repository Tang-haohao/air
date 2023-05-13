#demo/api/models.py 
from django.db import models

 
class Flight(models.Model):
    #The ID can be left blank. If you want to set it, you need to declare AutoField (primary_key=True)
	airCode =  models.CharField(max_length=100)
	create_time =  models.CharField(max_length=100)
	status =  models.CharField(max_length=100)
	reserve1 =  models.CharField(max_length=100)
	reserve2 =  models.CharField(max_length=100)
	reserve3 =  models.CharField(max_length=100)
	reserve4 =  models.CharField(max_length=100)
	reserve5 =  models.CharField(max_length=100)
	comCode =  models.CharField(max_length=100)
	flag =  models.CharField(max_length=100)
	fliAaddress =  models.CharField(max_length=100)
	fliAtime =  models.CharField(max_length=100)
	fliBaddress =  models.CharField(max_length=100)
	fliBtime =  models.CharField(max_length=100)
	fliCfare =  models.CharField(max_length=100)
	fliCnumber =  models.CharField(max_length=100)
	fliDiscount =  models.CharField(max_length=100)
	fliFfare =  models.CharField(max_length=100)
	fliFnumber =  models.CharField(max_length=100)
	fliNo =  models.CharField(max_length=100)
	fliRefundtime =  models.CharField(max_length=100)
	fliYfare =  models.CharField(max_length=100)
	fliYnumber =  models.CharField(max_length=100)
	class Meta:
		db_table = 'flight'
		verbose_name = "Flight"
		verbose_name_plural = verbose_name
	def __str__(self):  
		return ""