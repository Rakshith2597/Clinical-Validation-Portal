from django.db import models
import uuid
# Create your models here.
class MR_Likter(models.Model):
    ''' Model representing Image to be displayed '''
    q_id = models.IntegerField(primary_key = True)
    dataset = models.CharField(max_length = 50)
    organ = models.CharField(max_length = 50)
    original_image = models.FileField(upload_to='originalimage', blank=False)
    image = models.FileField(upload_to='image_one',blank=False)
    image_format = models.CharField(choices=(('MIRIAD', 'MIRIAD'),('JPEG', 'JPEG'),('J2K', 'J2K')), max_length=10)
    alpha_value = models.FloatField(blank=True, null = True)
    beta_value = models.FloatField(blank=True, null = True)
    hauffman_coding = models.CharField(choices=(('Y', 'Yes'),('N', 'No')), max_length=12, blank=True, null=True)
    bit_depth = models.FloatField(blank=True, null=True)
    quantizer_bit_depth = models.FloatField(blank=True, null=True)
    compression_factor = models.FloatField(blank=True, null=True)
    

    def __str__(self):
        '''String representing the model object'''
        return f'MR from {self.dataset}'

class CT_Likter(models.Model):
    ''' Model representing Image to be displayed '''
    q_id = models.IntegerField(primary_key = True)
    dataset = models.CharField(max_length = 50)
    organ = models.CharField(max_length = 50)
    original_image = models.FileField(upload_to='originalimage', blank=False)
    image = models.FileField(upload_to='image_one',blank=False)
    image_format = models.CharField(choices=(('MIRIAD', 'MIRIAD'),('JPEG', 'JPEG'),('J2K', 'J2K')), max_length=10)
    alpha_value = models.FloatField(blank=True, null = True)
    beta_value = models.FloatField(blank=True, null = True)
    hauffman_coding = models.CharField(choices=(('Y', 'Yes'),('N', 'No')), max_length=12, blank=True, null=True)
    bit_depth = models.FloatField(blank=True, null=True)
    quantizer_bit_depth = models.FloatField(blank=True, null=True)
    compression_factor = models.FloatField(blank=True, null=True)
    

    def __str__(self):
        '''String representing the model object'''
        return f'MR from {self.dataset}'

class XR_Likter(models.Model):
    ''' Model representing Image to be displayed '''
    q_id = models.IntegerField(primary_key = True)
    dataset = models.CharField(max_length = 50)
    organ = models.CharField(max_length = 50)
    original_image = models.FileField(upload_to='originalimage', blank=False)
    image = models.FileField(upload_to='image_one',blank=False)
    image_format = models.CharField(choices=(('MIRIAD', 'MIRIAD'),('JPEG', 'JPEG'),('J2K', 'J2K')), max_length=10)
    alpha_value = models.FloatField(blank=True, null = True)
    beta_value = models.FloatField(blank=True, null = True)
    hauffman_coding = models.CharField(choices=(('Y', 'Yes'),('N', 'No')), max_length=12, blank=True, null=True)
    bit_depth = models.FloatField(blank=True, null=True)
    quantizer_bit_depth = models.FloatField(blank=True, null=True)
    compression_factor = models.FloatField(blank=True, null=True)
    

    def __str__(self):
        '''String representing the model object'''
        return f'MR from {self.dataset}'

class Testresult_Likter(models.Model):
    username = models.CharField(max_length=50, default="")
    modality = models.CharField(max_length=50, default="")
    dataset = models.CharField(max_length=50, default="")
    image_quid = models.IntegerField(default=0)
    image = models.CharField(max_length=50, default="")
    image_format = models.CharField(max_length=50, default="")
    alpha_value = models.FloatField(blank=True, null=True)
    beta_value = models.FloatField(blank=True, null=True)
    hauffman_coding = models.CharField(max_length=50, blank=True, null=True)
    bit_depth = models.FloatField(blank=True, null=True)
    quantizer_bit_depth = models.FloatField(blank=True, null=True)
    compression_factor = models.FloatField(blank=True, null = True)
    original_image = models.CharField(max_length = 50, default = "")
    score = models.IntegerField(default = 0)

    def __str__(self):

        return f'Result Added of {self.dataset}'

class UserProgress_Likter(models.Model):
    username = models.CharField(max_length=50,)
    mr_progress = models.IntegerField(default=0)
    ct_progress = models.IntegerField(default=0)
    xr_progress = models.IntegerField(default=0)

    def __str__(self):

        return f'progress updated'