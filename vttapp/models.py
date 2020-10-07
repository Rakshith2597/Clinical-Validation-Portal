from django.db import models
import uuid
# Create your models here.
class MR(models.Model):
	''' Model representing Image to be displayed '''
	q_id = models.IntegerField(primary_key=True)
	dataset = models.CharField(max_length=50)
	our_image = models.FileField(upload_to='miriadimage',blank=False)
	jpeg_image = models.FileField(upload_to='jpegimage',blank=False)
	original_image = models.FileField(upload_to='originalimage',blank=False)

	def __str__(self):
		'''String representing the model object'''
		return f'MR from {self.dataset}'

class CT(models.Model):
	''' Model representing Image to be displayed '''
	q_id = models.IntegerField(primary_key=True)
	dataset = models.CharField(max_length=50)
	our_image = models.FileField(upload_to='miriadimage',blank=False)
	jpeg_image = models.FileField(upload_to='jpegimage',blank=False)
	original_image = models.FileField(upload_to='originalimage',blank=False)

	def __str__(self):
		'''String representing the model object'''
		return f'CT from {self.dataset}'

class XR(models.Model):
	''' Model representing Image to be displayed '''
	q_id = models.IntegerField(primary_key=True)
	dataset = models.CharField(max_length=50)
	miriad_image = models.FileField(upload_to='miriadimage',blank=False)
	jpeg_image = models.FileField(upload_to='jpegimage',blank=False)
	original_image = models.FileField(upload_to='originalimage',blank=False)

	def __str__(self):
		'''String representing the model object'''
		return f'XR from {self.dataset}'

class Testresult(models.Model):
	username = models.CharField(max_length=50, default="")
	dataset = models.CharField(max_length=50, default="")
	selcted_image = models.CharField(max_length=50, default="")
	confidence = models.IntegerField(default=0)

	def __str__(self):

		return f'Result Added of {self.dataset}'

class UserProgress(models.Model):
	username = models.CharField(max_length=50,)
	# progress = models.IntegerField(default=0)
	mr_progress = models.IntegerField(default=0)
	ct_progress = models.IntegerField(default=0)
	xr_progress = models.IntegerField(default=0)

	def __str__(self):

		return f'progress updated'

class ResponseSheet(models.Model):
	dataset = models.CharField(max_length=50)
	total_pass = models.IntegerField(default=0)
	total_fail = models.IntegerField(default=0)
	total_fail2 = models.IntegerField(default=0)
	option3_count = models.IntegerField(default=0)
	avg_confidence = models.IntegerField(default=0)

	def __str__(self):
		return f'Response table updated'