from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from vttapp.models import MR,CT,XR,Testresult,UserProgress,UserRequest
from WP3.models import UserProgress_WP3,Testresult_WP3
from django.contrib.auth.models import User

# Create your views here.
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

	tc_progress = (tc_qns/(total_qns or not total_qns))*100

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

@login_required
def dashboard_admin(request):
	num_users= User.objects.all().count()
	num_requests = UserRequest.objects.all().count()
	usr_status= UserProgress.objects.all()
	usr_status2= UserProgress_WP3.objects.all()
	

	context ={
				'user_counts': num_users,
				'p_requests' : num_requests,
				'usr_status' : usr_status,
				'usr_status2' : usr_status2,
				'user_name' : request.user,
	}

	return render(request,'dashboard_admin.html',context)


@login_required
def dashboard_admin_wp1(request):
	num_users= User.objects.all().count()
	num_requests = UserRequest.objects.all().count()
	usr_status= UserProgress.objects.all()
	t_response = Testresult.objects.all()

	context ={
				'user_counts': num_users,
				'p_requests' : num_requests,
				'usr_status' : usr_status,
				't_response' : t_response,
				'user_name' : request.user,
	}

	return render(request,'dashboard_admin_wp1.html',context)

@login_required
def dashboard_admin_wp3(request):
	num_users= User.objects.all().count()
	num_requests = UserRequest.objects.all().count()
	usr_status= UserProgress_WP3.objects.all()
	t_response = Testresult_WP3.objects.all()

	context ={
				'user_counts': num_users,
				'p_requests' : num_requests,
				'usr_status' : usr_status,
				't_response' : t_response,
				'user_name' : request.user,
	}

	return render(request,'dashboard_admin_wp3.html',context)