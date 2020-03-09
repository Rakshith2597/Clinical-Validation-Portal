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