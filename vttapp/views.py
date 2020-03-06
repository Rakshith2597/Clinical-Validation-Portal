from django.shortcuts import render,redirect
from django.views import generic
from vttapp.models import XR
import random

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

def XR(request):
	num_pairs = q_id.objects.count()
	im_no = random.randint(0,num_pairs)

	return render(request,'app1.html')