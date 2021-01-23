from django.db import models

# Create your models here.
class Facedb(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=255)
	click = models.CharField(max_length=255)


	def __str__(self):
		return self.summary+'-->'+self.click			#--> will be shown in database doesnot effect anything

	# def __str__(self):			#this is also right with different __str__ return
	# 	return self.click

		
