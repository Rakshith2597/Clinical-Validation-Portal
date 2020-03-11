from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('CT/', views.CT_func, name='CT'),
	path('MR/', views.MR_func, name='MR'),
	path('XR/', views.XR_func, name='XR'),
	# path('XR/<int:count>', views.XR_func, name='XR'),


]
