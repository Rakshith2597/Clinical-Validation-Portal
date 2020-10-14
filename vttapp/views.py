from django.shortcuts import render,redirect
from django.views import generic
from vttapp.models import MR,CT,XR,Testresult,UserProgress,ResponseSheet
import random
from django.conf import settings
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration
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

				form.selcted_image = request.POST.get('selcted_image')
				form.username = request.user
				form.dataset = img_field.dataset
				form.image_quid = img_field.q_id
				form.confidence = request.POST.get('confidence')
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

				form.selcted_image = request.POST.get('selcted_image')
				form.username = request.user
				form.dataset = img_field.dataset
				form.image_quid = img_field.q_id
				form.confidence = request.POST.get('confidence')
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

				form.selcted_image = request.POST.get('selcted_image')
				form.username = request.user
				form.dataset = img_field.dataset
				form.image_quid = img_field.q_id
				form.confidence = request.POST.get('confidence')
				usr_row.ct_progress = usr_progress+1
				usr_row.save(update_fields=['ct_progress'])
				form.save()
		return render(request,'app3.html',context)
	else:
		return render(request,'completion.html')		

def response_func(request):
	t_response = Testresult.objects.all()
	dataset_list = ['cbis','mura','luna','chexpert','isles18','isles17','mrnet','chaosct','chaosmr']

	for dataset_name in dataset_list:
		real_count = Testresult.objects.filter(dataset__istartswith=dataset_name,selcted_image__icontains='Ours').count()
		fake_count = Testresult.objects.filter(dataset__istartswith=dataset_name,selcted_image__icontains='Jpeg').count()
		fake_count2 = Testresult.objects.filter(dataset__istartswith=dataset_name,selcted_image__icontains='J2k').count()
		option3_count = Testresult.objects.filter(dataset__istartswith=dataset_name,selcted_image__icontains='Equal').count()
		avg_confidence = Testresult.objects.filter(dataset__istartswith=dataset_name).aggregate(Avg('confidence'))
		response_element = ResponseSheet.objects.filter(dataset__istartswith=dataset_name)
		for elem in response_element:
			elem.total_pass = real_count
			elem.total_fail = fake_count
			elem.total_fail2 = fake_count2
			elem.option3_count = option3_count
			if avg_confidence['confidence__avg']:
				elem.avg_confidence = avg_confidence['confidence__avg']
			else:
				elem.avg_confidence = 0
			
			elem.save(update_fields=['total_pass','total_fail','total_fail2','option3_count','avg_confidence'])

	response_table = ResponseSheet.objects.all()

	context = {
	'response_table' : response_table,
	'display' : "none",
	}

	if request.method == 'POST':
			context = {
			'response_table' : response_table,
			'query_results' : t_response,
			'display' : "block",


			}


	return render(request,'response.html',context)

def register_user(request):

	form2 = UserRegistration()
	context = {'form': form2}

	if request.method == 'POST':
		f_instance = UserRegistration(request.POST)
		if f_instance.is_valid():
			new_instance = f_instance.save(commit=False)
			new_instance.save()


	return render(request,'register.html',context)


@login_required
def dashboard(request):
	XR_qns = XR.objects.all().count()
	CT_qns = CT.objects.all().count()
	MR_qns = MR.objects.all().count()

	total_qns = XR_qns+CT_qns+MR_qns

	user_name = request.user
	usr_status= UserProgress.objects.get(username=request.user)
	XR_status = usr_status.xr_progress
	CT_status = usr_status.ct_progress
	MR_status = usr_status.mr_progress


	tc_qns = XR_status+CT_status+MR_status
	if XR_qns != 0:
		XR_progress = (XR_status/XR_qns)*100
	else:
		XR_progress = 0
	if CT_qns != 0:
		CT_progress = (CT_status/CT_qns)*100
	else:
		CT_progress = 0
	if MR_qns != 0:
		MR_progress = (MR_status/MR_qns)*100
	else:
		MR_progress = 0

	tc_progress = (tc_qns/total_qns)*100

	context ={
				'total_qns': total_qns,
				'user_name': user_name,
				'tc_qns': tc_qns,
				'XR_progress':XR_progress,
				'CT_progress':CT_progress,
				'MR_progress':MR_progress,
				'tc_progress':tc_progress,
	}


	return render(request,'dashboard.html',context)