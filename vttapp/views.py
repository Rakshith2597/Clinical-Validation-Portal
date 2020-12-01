from django.shortcuts import render,redirect
from django.views import generic
from vttapp.models import MR,CT,XR,Testresult,UserProgress,UserRequest
import random
from django.conf import settings
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration
from django.contrib.auth.models import User
# Create your views here.
def index(request):
	return render(request,'index.html')


@login_required
def XR_func(request):
	num_pairs = XR.objects.all().count()
	usr_row = UserProgress.objects.get(username=request.user)
	usr_progress = usr_row.xr_progress 
	if usr_progress <= num_pairs-1:
		img_field = XR.objects.get(q_id = usr_progress)
		imageone_url = img_field.image_one.url
		imagetwo_url = img_field.image_two.url
		originalimg_url = img_field.original_image.url
		organ = img_field.organ

		imageone_name = img_field.image_one.name
		imagetwo_name = img_field.image_two.name
		originalimg_name = img_field.original_image.name
		if usr_progress%3 != 0:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : imageone_url,
			'image2_url' : imagetwo_url,
			'image3_url' : originalimg_url,
 			'image1_name' : imageone_name,
			'image2_name' : imagetwo_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "XR",
			'organ': organ,
			}
		else:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : imagetwo_url,
			'image2_url' : imageone_url,
			'image3_url' : originalimg_url,
			'image1_name' : imagetwo_name,
			'image2_name' : imageone_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "XR",
			'organ': organ,
			}	


		if request.method == 'POST':

			form = Testresult()
			if request.POST.get('selcted_image') and request.POST.get('confidence'):

				form.selected_image = request.POST.get('selcted_image')
				form.username = request.user
				form.modality = "XR"
				form.dataset = img_field.dataset
				form.image_quid = img_field.q_id
				form.image_one = img_field.image_one
				form.image_one_format = img_field.image_one_format
				form.image_two = img_field.image_two
				form.image_two_format = img_field.image_two_format
				form.confidence = request.POST.get('confidence')
				form.alpha_value = img_field.alpha_value
				form.beta_value = img_field.beta_value
				form.hauffman_coding = img_field.hauffman_coding
				form.bit_depth = img_field.bit_depth
				form.quantizer_bit_depth = img_field.quantizer_bit_depth
				form.compression_factor_image1 = img_field.compression_factor_image1
				form.compression_factor_image2 = img_field.compression_factor_image2

				usr_row.xr_progress = usr_progress+1
				usr_row.save(update_fields=['xr_progress'])
				form.save()
		return render(request,'app1.html',context)
	else:
		return render(request,'completion.html')

@login_required
def MR_func(request):
	num_pairs = MR.objects.all().count()
	usr_row = UserProgress.objects.get(username=request.user)
	usr_progress = usr_row.mr_progress 
	if usr_progress <= num_pairs-1:
		img_field = MR.objects.get(q_id = usr_progress)
		imageone_url = img_field.image_one.url
		imagetwo_url = img_field.image_two.url
		originalimg_url = img_field.original_image.url
		organ = img_field.organ

		imageone_name = img_field.image_one.name
		imagetwo_name = img_field.image_two.name
		originalimg_name = img_field.original_image.name
		if usr_progress%3 != 0:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : imageone_url,
			'image2_url' : imagetwo_url,
			'image3_url' : originalimg_url,
 			'image1_name' : imageone_name,
			'image2_name' : imagetwo_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "MR",
			'organ': organ,
			}
		else:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : imagetwo_url,
			'image2_url' : imageone_url,
			'image3_url' : originalimg_url,
			'image1_name' : imagetwo_name,
			'image2_name' : imageone_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "MR",
			'organ': organ,
			}


		if request.method == 'POST':

			form = Testresult()
			if request.POST.get('selcted_image') and request.POST.get('confidence'):

				form.selected_image = request.POST.get('selcted_image')
				form.username = request.user
				form.modality = "MR"
				form.dataset = img_field.dataset
				form.image_quid = img_field.q_id
				form.image_one = img_field.image_one.name
				form.image_one_format = img_field.image_one_format
				form.image_two = img_field.image_two.name
				form.image_two_format = img_field.image_two_format
				form.confidence = request.POST.get('confidence')
				form.alpha_value = img_field.alpha_value
				form.beta_value = img_field.beta_value
				form.hauffman_coding = img_field.hauffman_coding
				form.bit_depth = img_field.bit_depth
				form.quantizer_bit_depth = img_field.quantizer_bit_depth
				form.compression_factor_image1 = img_field.compression_factor_image1
				form.compression_factor_image2 = img_field.compression_factor_image2

				usr_row.mr_progress = usr_progress+1
				usr_row.save(update_fields=['mr_progress'])
				form.save()
		return render(request,'app2.html',context)
	else:
		return render(request,'completion.html')

@login_required
def CT_func(request):
	num_pairs = CT.objects.all().count()
	usr_row = UserProgress.objects.get(username=request.user)
	usr_progress = usr_row.ct_progress 
	if usr_progress <= num_pairs-1:
		img_field = CT.objects.get(q_id = usr_progress)
		organ = img_field.organ
		imageone_url = img_field.image_one.url
		imagetwo_url = img_field.image_two.url
		originalimg_url = img_field.original_image.url

		imageone_name = img_field.image_one.name
		imagetwo_name = img_field.image_two.name
		originalimg_name = img_field.original_image.name
		if usr_progress%3 != 0:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : imageone_url,
			'image2_url' : imagetwo_url,
			'image3_url' : originalimg_url,
 			'image1_name' : imageone_name,
			'image2_name' : imagetwo_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "CT",
			'organ': organ,
			}
		else:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : imagetwo_url,
			'image2_url' : imageone_url,
			'image3_url' : originalimg_url,
			'image1_name' : imagetwo_name,
			'image2_name' : imageone_name,
			'image3_name' : originalimg_name,
			'usr_progress' : usr_progress,
			'num_pairs' : num_pairs,
			'action' : "CT",
			'organ': organ,
			}	


		if request.method == 'POST':

			form = Testresult()
			if request.POST.get('selcted_image') and request.POST.get('confidence'):

				form.selected_image = request.POST.get('selcted_image')
				form.username = request.user
				form.modality = "CT"
				form.dataset = img_field.dataset
				form.image_quid = img_field.q_id
				form.image_one = img_field.image_one.name
				form.image_one_format = img_field.image_one_format
				form.image_two = img_field.image_two.name
				form.image_two_format = img_field.image_two_format
				form.confidence = request.POST.get('confidence')
				form.alpha_value = img_field.alpha_value
				form.beta_value = img_field.beta_value
				form.hauffman_coding = img_field.hauffman_coding
				form.bit_depth = img_field.bit_depth
				form.quantizer_bit_depth = img_field.quantizer_bit_depth
				form.compression_factor_image1 = img_field.compression_factor_image1
				form.compression_factor_image2 = img_field.compression_factor_image2

				usr_row.ct_progress = usr_progress+1
				usr_row.save(update_fields=['ct_progress'])
				form.save()
		return render(request,'app3.html',context)
	else:
		return render(request,'completion.html')		

def register_user(request):

	form2 = UserRegistration()
	context = {'form': form2}

	if request.method == 'POST':
		f_instance = UserRegistration(request.POST)
		if f_instance.is_valid():
			new_instance = f_instance.save(commit=False)
			new_instance.save()
		return render(request,'register_sucess.html')


	return render(request,'register.html',context)
