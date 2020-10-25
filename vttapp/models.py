from django.db import models
import uuid
# Create your models here.

class MR(models.Model):
	''' Model representing Image to be displayed '''
	q_id = models.IntegerField(primary_key=True)
	dataset = models.CharField(max_length=50)
	organ = models.CharField(max_length=50)
	image_one = models.FileField(upload_to='image_one',blank=False)
	image_one_format = models.CharField(choices=(('MIRIAD', 'MIRIAD'),('JPEG', 'JPEG'),('J2K', 'J2K')), max_length=10)
	image_two = models.FileField(upload_to='image_two',blank=False)
	image_two_format = models.CharField(choices=(('MIRIAD', 'MIRIAD'),('JPEG', 'JPEG'),('J2K', 'J2K')), max_length=10)
	alpha_value = models.FloatField(blank=True,null=True)
	beta_value = models.FloatField(blank=True,null=True)
	hauffman_coding = models.CharField(choices=(('Y', 'Yes'),('N', 'No')), max_length=12,blank=True,null=True)
	bit_depth = models.IntegerField(blank=True,null=True)
	quantizer_bit_depth = models.IntegerField(blank=True,null=True)
	compression_factor = models.IntegerField(blank=True,null=True)
	quality_factor = models.IntegerField(blank=True,null=True)
	original_image = models.FileField(upload_to='originalimage',blank=False)

	def __str__(self):
		'''String representing the model object'''
		return f'MR from {self.dataset}'

class CT(models.Model):
	''' Model representing Image to be displayed '''
	q_id = models.IntegerField(primary_key=True)
	dataset = models.CharField(max_length=50)
	organ = models.CharField(max_length=50)
	image_one = models.FileField(upload_to='image_one',blank=False)
	image_one_format = models.CharField(choices=(('MIRIAD', 'MIRIAD'),('JPEG', 'JPEG'),('J2K', 'J2K')), max_length=10)
	image_two = models.FileField(upload_to='image_two',blank=False)
	image_two_format = models.CharField(choices=(('MIRIAD', 'MIRIAD'),('JPEG', 'JPEG'),('J2K', 'J2K')), max_length=10)
	alpha_value = models.FloatField(blank=True,null=True)
	beta_value = models.FloatField(blank=True,null=True)
	hauffman_coding = models.CharField(choices=(('Y', 'Yes'),('N', 'No')), max_length=12,blank=True,null=True)
	bit_depth = models.IntegerField(blank=True,null=True)
	quantizer_bit_depth = models.IntegerField(blank=True,null=True)
	compression_factor = models.IntegerField(blank=True,null=True)
	quality_factor = models.IntegerField(blank=True,null=True)
	original_image = models.FileField(upload_to='originalimage',blank=False)

	def __str__(self):
		'''String representing the model object'''
		return f'CT from {self.dataset}'

class XR(models.Model):
	''' Model representing Image to be displayed '''
	q_id = models.IntegerField(primary_key=True)
	dataset = models.CharField(max_length=50)
	organ = models.CharField(max_length=50)
	image_one = models.FileField(upload_to='image_one',blank=False)
	image_one_format = models.CharField(choices=(('MIRIAD', 'MIRIAD'),('JPEG', 'JPEG'),('J2K', 'J2K')), max_length=10)
	image_two = models.FileField(upload_to='image_two',blank=False)
	image_two_format = models.CharField(choices=(('MIRIAD', 'MIRIAD'),('JPEG', 'JPEG'),('J2K', 'J2K')), max_length=10)
	alpha_value = models.FloatField(blank=True,null=True)
	beta_value = models.FloatField(blank=True,null=True)
	hauffman_coding = models.CharField(choices=(('Y', 'Yes'),('N', 'No')), max_length=12,blank=True,null=True)
	bit_depth = models.IntegerField(blank=True,null=True)
	quantizer_bit_depth = models.IntegerField(blank=True,null=True)
	compression_factor = models.IntegerField(blank=True,null=True)
	quality_factor = models.IntegerField(blank=True,null=True)
	original_image = models.FileField(upload_to='originalimage',blank=False)

	def __str__(self):
		'''String representing the model object'''
		return f'XR from {self.dataset}'

class Testresult(models.Model):
	username = models.CharField(max_length=50, default="")
	modality = models.CharField(max_length=50, default="")
	dataset = models.CharField(max_length=50, default="")
	image_quid = models.IntegerField(default=0)
	image_one = models.CharField(max_length=50, default="")
	image_one_format = models.CharField(max_length=50, default="")
	image_two = models.CharField(max_length=50, default="")
	image_two_format = models.CharField(max_length=50, default="")
	alpha_value = models.FloatField(blank=True,null=True)
	beta_value = models.FloatField(blank=True,null=True)
	hauffman_coding = models.CharField(max_length=50,blank=True,null=True)
	bit_depth = models.IntegerField(blank=True,null=True)
	quantizer_bit_depth = models.IntegerField(blank=True,null=True)
	compression_factor = models.IntegerField(blank=True,null=True)
	quality_factor = models.IntegerField(blank=True,null=True)
	original_image = models.CharField(max_length=50, default="")
	selected_image = models.CharField(max_length=50, default="")
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

class UserRequest(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	designation = models.CharField(max_length=50)
	registration_number = models.CharField(max_length=50)
	email_id = models.CharField(max_length=50)

	def __str__(self):
		return f'New Request'
