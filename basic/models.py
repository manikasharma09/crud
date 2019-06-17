from django.db import models

class Profile(models.Model):
	id_no=models.CharField(max_length=100,primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	college_name=models.CharField(max_length=100)
	cgpa=models.IntegerField()
	password=models.CharField(max_length=100)

	
