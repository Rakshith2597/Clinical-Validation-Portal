from django.shortcuts import render,redirect
from WP3.models import WP3_Questions,Testresult_WP3,UserProgress_WP3
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
	return render(request,'index_wp3.html')

@login_required
def wp3_test(request):
	num_qstns = WP3_Questions.objects.all().count()
	usr_row = UserProgress_WP3.objects.get(username=request.user)
	usr_progress = usr_row.progress 
	if usr_progress <= num_qstns-1:
		img_field = WP3_Questions.objects.get(q_id = usr_progress)
		image_one_url = img_field.image_one.url
		image_two_url = img_field.image_two.url
		image_three_url = img_field.image_two.url
		image_four_url = img_field.image_two.url
		original_img_url = img_field.original_image.url

		image_one_name = img_field.image_one.name
		image_two_name = img_field.image_two.name
		image_three_name = img_field.image_three.name
		image_four_name = img_field.image_four.name
		original_img_name = img_field.original_image.name

		if usr_progress%2 != 0:
			context = {
			'num_qstns' : num_qstns,
			'image1_url' : image_one_url,
			'image2_url' : image_two_url,
			'image3_url' : image_three_url,
			'image4_url' : image_four_url,
			'original_img_url': original_img_url,
 			'image1_name' : image_one_name,
			'image2_name' : image_two_name,
			'image3_name' : image_three_name,
			'image4_name' : image_four_name,
			'original_img_name': original_img_name,
			'usr_progress' : usr_progress,
			'num_qstns' : num_qstns
			}
		else:
			context = {
			'num_qstns' : num_qstns,
			'image1_url' : image_four_url,
			'image2_url' : image_three_url,
			'image3_url' : image_one_url,
			'image4_url' : image_two_url,
			'original_img_url': original_img_url,
 			'image1_name' : image_four_name,
			'image2_name' : image_three_name,
			'image3_name' : image_one_name,
			'image4_name' : image_two_name,
			'original_img_name': original_img_name,
			'usr_progress' : usr_progress,
			'num_qstns' : num_qstns
			}	


		if request.method == 'POST':

			form = Testresult_WP3()
			# if request.POST.get('selcted_image') and request.POST.get('confidence'):

			
			form.username = request.user
			form.image_quid = img_field.q_id
			form.image_one = img_field.image_one
			form.image_one_net = img_field.image_one_net
			form.image_one_score = request.POST.get('score1')
			form.image_two = img_field.image_two
			form.image_two_net = img_field.image_two_net
			form.image_two_score = request.POST.get('score2')
			form.image_three = img_field.image_three
			form.image_three_net = img_field.image_three_net
			form.image_three_score = request.POST.get('score3')
			form.image_four = img_field.image_four
			form.image_four_net = img_field.image_four_net
			form.image_four_score = request.POST.get('score4')

			usr_row.progress = usr_progress+1
			usr_row.save(update_fields=['progress'])
			form.save()
		return render(request,'test_app.html',context)
	else:
		return render(request,'completion.html')


	return render(request,'test_app.html')

