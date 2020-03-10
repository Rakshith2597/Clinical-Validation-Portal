from django.shortcuts import render,redirect
from django.views import generic
from vttapp.models import XR,Testresult
import random
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	return render(request,'index.html')


@login_required
def XR_func(request):
	num_pairs = XR.objects.all().count()
	img_field = XR.objects.get(q_id = 101)
	realimg_url = img_field.real_image.url
	fakeimg_url = img_field.fake_image.url
	realimg_name = img_field.real_image.name
	fakeimg_name = img_field.fake_image.name
	context = {
	'num_pairs' : num_pairs,
	'image1_url' : realimg_url,
	'image2_url' : fakeimg_url,
	'image1_name' : realimg_name,
	'image2_name' : fakeimg_name,
	}

	if request.method == 'POST':

		form = Testresult()
		if request.POST.get('selcted_image') and request.POST.get('confidence'):

			form.selcted_image = request.POST.get('selcted_image')
			form.username = request.user
			form.dataset = img_field.dataset
			form.confidence = request.POST.get('confidence')
			form.save()
	return render(request,'app1.html',context)


