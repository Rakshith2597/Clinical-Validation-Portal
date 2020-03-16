from django.shortcuts import render,redirect
from django.views import generic
from vttapp.models import MR,CT,XR,Testresult,UserProgress,ResponseSheet
import random
from django.conf import settings
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
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
		realimg_url = img_field.real_image.url
		fakeimg_url = img_field.fake_image.url
		realimg_name = img_field.real_image.name
		fakeimg_name = img_field.fake_image.name
		if usr_progress%3 != 0:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : realimg_url,
			'image2_url' : fakeimg_url,
			'image1_name' : realimg_name,
			'image2_name' : fakeimg_name,
			'action' : "XR",
			}
		else:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : fakeimg_url,
			'image2_url' : realimg_url,
			'image1_name' : fakeimg_name,
			'image2_name' : realimg_name,
			'action' : "XR",
			}	


		if request.method == 'POST':

			form = Testresult()
			if request.POST.get('selcted_image') and request.POST.get('confidence'):

				form.selcted_image = request.POST.get('selcted_image')
				form.username = request.user
				form.dataset = img_field.dataset
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
		realimg_url = img_field.real_image.url
		fakeimg_url = img_field.fake_image.url
		realimg_name = img_field.real_image.name
		fakeimg_name = img_field.fake_image.name
		if usr_progress%3 != 0:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : realimg_url,
			'image2_url' : fakeimg_url,
			'image1_name' : realimg_name,
			'image2_name' : fakeimg_name,
			'action' : "XR",
			}
		else:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : fakeimg_url,
			'image2_url' : realimg_url,
			'image1_name' : fakeimg_name,
			'image2_name' : realimg_name,
			'action' : "XR",
			}	


		if request.method == 'POST':

			form = Testresult()
			if request.POST.get('selcted_image') and request.POST.get('confidence'):

				form.selcted_image = request.POST.get('selcted_image')
				form.username = request.user
				form.dataset = img_field.dataset
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
		realimg_url = img_field.real_image.url
		fakeimg_url = img_field.fake_image.url
		realimg_name = img_field.real_image.name
		fakeimg_name = img_field.fake_image.name
		if usr_progress%3 != 0:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : realimg_url,
			'image2_url' : fakeimg_url,
			'image1_name' : realimg_name,
			'image2_name' : fakeimg_name,
			'action' : "XR",
			}
		else:
			context = {
			'num_pairs' : num_pairs,
			'image1_url' : fakeimg_url,
			'image2_url' : realimg_url,
			'image1_name' : fakeimg_name,
			'image2_name' : realimg_name,
			'action' : "XR",
			}	


		if request.method == 'POST':

			form = Testresult()
			if request.POST.get('selcted_image') and request.POST.get('confidence'):

				form.selcted_image = request.POST.get('selcted_image')
				form.username = request.user
				form.dataset = img_field.dataset
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
		real_count = Testresult.objects.filter(dataset__istartswith=dataset_name,selcted_image__istartswith='Real').count()
		fake_count = Testresult.objects.filter(dataset__istartswith=dataset_name,selcted_image__istartswith='Fake').count()
		avg_confidence = Testresult.objects.filter(dataset__istartswith=dataset_name).aggregate(Avg('confidence'))
		response_element = ResponseSheet.objects.filter(dataset__istartswith=dataset_name)
		for elem in response_element:
			elem.total_pass = real_count
			elem.total_fail = fake_count
			if avg_confidence['confidence__avg']:
				elem.avg_confidence = avg_confidence['confidence__avg']
			else:
				elem.avg_confidence = 0
			
			elem.save(update_fields=['total_pass','total_fail','avg_confidence'])

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


