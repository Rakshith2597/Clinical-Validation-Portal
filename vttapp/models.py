from django.db import models
import uuid
# Create your models here.
class MR(models.Model):
	''' Model representing Image to be displayed '''
	q_id = models.IntegerField(primary_key=True)
	dataset = models.CharField(max_length=50)
	real_image = models.FileField(upload_to='realimage',blank=False)
	fake_image = models.FileField(upload_to='fakeimage',blank=False)

	def __str__(self):
		'''String representing the model object'''
		return f'MR from {self.dataset}'

class CT(models.Model):
	''' Model representing Image to be displayed '''
	q_id = models.IntegerField(primary_key=True)
	dataset = models.CharField(max_length=50)
	real_image = models.FileField(upload_to='realimage',blank=False)
	fake_image = models.FileField(upload_to='fakeimage',blank=False)

	def __str__(self):
		'''String representing the model object'''
		return f'CT from {self.dataset}'

class XR(models.Model):
	''' Model representing Image to be displayed '''
	q_id = models.IntegerField(primary_key=True)
	dataset = models.CharField(max_length=50)
	real_image = models.FileField(upload_to='realimage',blank=False)
	fake_image = models.FileField(upload_to='fakeimage',blank=False)

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