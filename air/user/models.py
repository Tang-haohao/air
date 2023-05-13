#demo/api/models.py 
from django.db import models

 
class User(models.Model):
    #The ID can be left blank. If you want to set it, you need to declare AutoField (primary_key=True)
	username =  models.CharField(max_length=100)
	name =  models.CharField(max_length=100)
	password =  models.CharField(max_length=100)
	role = models.IntegerField()
	status =  models.CharField(max_length=100)
	reserve1 =  models.CharField(max_length=100)
	reserve2 =  models.CharField(max_length=100)
	reserve3 =  models.CharField(max_length=100)
	reserve4 =  models.CharField(max_length=100)
	reserve5 =  models.CharField(max_length=100)
	create_time =  models.CharField(max_length=100)
	class Meta:
		db_table = 'user'
		verbose_name = "User"
		verbose_name_plural = verbose_name
	def __str__(self):  
		return ""