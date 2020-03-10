from django.shortcuts import render,redirect
from django.views import generic
from vttapp.models import XR,Testresult
import random
from django.conf import settings
from django.contrib.auth.decorators import login_required
from vttapp.forms import TuringTest
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

@login_required
def XR_func(request):



	num_pairs = XR.objects.all().count()
	# for i in range(1,num_pairs):
	# 	img_id = 100 + i 

	img_field = XR.objects.get(q_id = 101)
	# initial_path1 = img_field.real_image.path
	# initial_path2 = img_field.fake_image.path


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
	form = TuringTest(instance=Testresult)

	if request.method == 'POST':
		form = TuringTest(request.POST, instance=Testresult)

		if form.is_valid():
			# print("helloo")
			Testresult.selcted_image = form.cleaned_data['selcted_image']
			Testresult.username = request.user
			Testresult.dataset = img_field.dataset
			Testresult.confidence = form.cleaned_data['confidence']
			Testresult.save()
			return redirect('XR_func')
		else:
			return render(request,'app1', {'form': form})

	else:
		return render(request,'app1.html',context=context)

	
