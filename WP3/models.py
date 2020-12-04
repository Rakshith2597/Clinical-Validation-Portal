from django.db import models

# Create your models here.

networks = (('Xception', 'Xception'),('ResNet', 'ResNet'),
	('DenseNet', 'DenseNet'),('EfficientNet','EfficientNet'))
		
class WP3_Questions(models.Model):

	q_id = models.IntegerField(primary_key=True)
	anomaly = models.CharField(default="",max_length=16)
	original_image = models.FileField(upload_to='image_one',blank=False)
	image_one = models.FileField(upload_to='image_one',blank=False)
	image_one_net = models.CharField(choices=networks, max_length=16)
	image_two = models.FileField(upload_to='image_two',blank=False)
	image_two_net = models.CharField(choices=networks, max_length=16)
	image_three = models.FileField(upload_to='image_three',blank=False)
	image_three_net = models.CharField(choices=networks, max_length=16)
	image_four = models.FileField(upload_to='image_four',blank=False)
	image_four_net = models.CharField(choices=networks, max_length=16)

	def __str__(self):
		'''String representing the model object'''
		return f'Question no:{self.q_id}'



class Testresult_WP3(models.Model):
	username = models.CharField(max_length=50, default="")
	image_quid = models.IntegerField(default=0)
	anomaly = models.CharField(default="",max_length=16)
	image_one = models.FileField(upload_to='image_one',blank=False)
	image_one_net = models.CharField(choices=networks, max_length=16)
	image_two = models.FileField(upload_to='image_two',blank=False)
	image_two_net = models.CharField(choices=networks, max_length=16)
	image_three = models.FileField(upload_to='image_three',blank=False)
	image_three_net = models.CharField(choices=networks, max_length=16)
	image_four = models.FileField(upload_to='image_four',blank=False)
	image_four_net = models.CharField(choices=networks, max_length=16)
	image_one_score = models.IntegerField(default=0)
	image_two_score = models.IntegerField(default=0)
	image_three_score = models.IntegerField(default=0)
	image_four_score = models.IntegerField(default=0)


	def __str__(self):

		return f'Result Added of {self.username}'



class UserProgress_WP3(models.Model):
	username = models.CharField(max_length=50,)
	progress = models.IntegerField(default=0)

	def __str__(self):

		return f'progress of {self.username}'