from django.shortcuts import render,redirect

# Create your views here.
def index(request):
	return render(request,'index_home.html')

def WP1(request):
	return redirect('/wp1/')

def WP1_likter(request):
	return redirect('/wp1_likter/')

def WP3(request):
	return redirect('/wp3/')
