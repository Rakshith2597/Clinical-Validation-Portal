from django.shortcuts import render,redirect

# Create your views here.

def index(request):
	return render(request,'index_wp3.html')


def wp3_test(request):


	return render(request,'test_app.html')

