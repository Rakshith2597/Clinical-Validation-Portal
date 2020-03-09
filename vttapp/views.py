from django.shortcuts import render,redirect
from django.views import generic
from vttapp.models import XR
import random
from django.conf import settings

# Create your views here.
def index(request):
	return render(request,'index.html')


class VTTApp(generic.View):
	def get(self,request):
		return render(request,'base.html')

	def post(self,request):
		return redirect("index")
	

# def CT(request):
# 	return render(request,'generic.html')

# def MR(request):
# 	return render(request,'generic.html')

def XR_func(request):
	num_pairs = XR.objects.all().count()
	i = num_pairs-1

	img_field = XR.objects.get(q_id = 101)
	# initial_path1 = img_field.real_image.path
	# initial_path2 = img_field.fake_image.path


	realimg_url = img_field.real_image.url
	fakeimg_url = img_field.fake_image.url
	context = {
	'num_pairs' : num_pairs,
	'image1_url' : realimg_url,
	'image2_url' : fakeimg_url,
	}

	return render(request,'app1.html',context=context)
