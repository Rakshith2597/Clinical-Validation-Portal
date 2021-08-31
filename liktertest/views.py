from django.shortcuts import render,redirect
from django.views import generic
from liktertest.models import MR_Likter, CT_Likter, XR_Likter, Testresult_Likter, UserProgress_Likter
import random
from django.conf import settings
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import csv
# Create your views here.
def index(request):
	return render(request,'index_likter.html')

@login_required
def XR_Likter_func(request):
	num_pairs = XR_Likter.objects.all().count()
	usr_row = UserProgress_Likter.objects.get(username = request.user)
	usr_progress = usr_row.xr_progress 
	if usr_progress <= num_pairs-1:
		img_field = XR_Likter.objects.get(q_id = usr_progress)
		image_url = img_field.image.url
		originalimg_url = img_field.original_image.url
		organ = img_field.organ

		image_name = img_field.image.name
		originalimg_name = img_field.original_image.name
		if usr_progress%3 != 0:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : image_url,
			'image3_url' : originalimg_url,
 			'image1_name' : image_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "XR",
			'organ': organ,
			}
		else:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : image_url,
			'image3_url' : originalimg_url,
			'image1_name' : image_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "XR",
			'organ': organ,
			}	


		if request.method == 'POST':

			form = Testresult_Likter()
			if request.POST.get('score'):
				form.score = request.POST.get('score')
				form.username = request.user
				form.modality = "XR"
				form.dataset = img_field.dataset
				form.image_quid = img_field.q_id
				form.image = img_field.image
				form.image_format = img_field.image_format
				form.alpha_value = img_field.alpha_value
				form.beta_value = img_field.beta_value
				form.hauffman_coding = img_field.hauffman_coding
				form.bit_depth = img_field.bit_depth
				form.quantizer_bit_depth = img_field.quantizer_bit_depth
				form.compression_factor = img_field.compression_factor

				usr_row.xr_progress = usr_progress + 1
				usr_row.save(update_fields=['xr_progress'])
				form.save()
		return render(request, 'likter_xr.html', context)
	else:
		return render(request,'completion_likter.html')

@login_required
def CT_Likter_func(request):
	num_pairs = CT_Likter.objects.all().count()
	usr_row = UserProgress_Likter.objects.get(username = request.user)
	usr_progress = usr_row.ct_progress 
	if usr_progress <= num_pairs-1:
		img_field = CT_Likter.objects.get(q_id = usr_progress)
		image_url = img_field.image.url
		originalimg_url = img_field.original_image.url
		organ = img_field.organ

		image_name = img_field.image.name
		originalimg_name = img_field.original_image.name
		if usr_progress%3 != 0:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : image_url,
			'image3_url' : originalimg_url,
 			'image1_name' : image_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "CT",
			'organ': organ,
			}
		else:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : image_url,
			'image3_url' : originalimg_url,
			'image1_name' : image_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "CT",
			'organ': organ,
			}	


		if request.method == 'POST':

			form = Testresult_Likter()
			if request.POST.get('score'):
				form.score = request.POST.get('score')
				form.username = request.user
				form.modality = "CT"
				form.dataset = img_field.dataset
				form.image_quid = img_field.q_id
				form.image = img_field.image
				form.image_format = img_field.image_format
				form.alpha_value = img_field.alpha_value
				form.beta_value = img_field.beta_value
				form.hauffman_coding = img_field.hauffman_coding
				form.bit_depth = img_field.bit_depth
				form.quantizer_bit_depth = img_field.quantizer_bit_depth
				form.compression_factor = img_field.compression_factor

				usr_row.ct_progress = usr_progress + 1
				usr_row.save(update_fields=['ct_progress'])
				form.save()
		return render(request,'likter_ct.html',context)
	else:
		return render(request,'completion_likter.html')

@login_required
def MR_Likter_func(request):
	num_pairs = MR_Likter.objects.all().count()
	usr_row = UserProgress_Likter.objects.get(username = request.user)
	usr_progress = usr_row.mr_progress 
	if usr_progress <= num_pairs-1:
		img_field = MR_Likter.objects.get(q_id = usr_progress)
		image_url = img_field.image.url
		originalimg_url = img_field.original_image.url
		organ = img_field.organ

		image_name = img_field.image.name
		originalimg_name = img_field.original_image.name
		if usr_progress%3 != 0:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : image_url,
			'image3_url' : originalimg_url,
 			'image1_name' : image_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "MR",
			'organ': organ,
			}
		else:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : image_url,
			'image3_url' : originalimg_url,
			'image1_name' : image_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "MR",
			'organ': organ,
			}	


		if request.method == 'POST':

			form = Testresult_Likter()
			if request.POST.get('score'):
				form.score = request.POST.get('score')
				form.username = request.user
				form.modality = "MR"
				form.dataset = img_field.dataset
				form.image_quid = img_field.q_id
				form.image = img_field.image
				form.image_format = img_field.image_format
				form.alpha_value = img_field.alpha_value
				form.beta_value = img_field.beta_value
				form.hauffman_coding = img_field.hauffman_coding
				form.bit_depth = img_field.bit_depth
				form.quantizer_bit_depth = img_field.quantizer_bit_depth
				form.compression_factor = img_field.compression_factor

				usr_row.mr_progress = usr_progress + 1
				usr_row.save(update_fields=['mr_progress'])
				form.save()
		return render(request,'likter_mr.html',context)
	else:
		return render(request,'completion_likter.html')
